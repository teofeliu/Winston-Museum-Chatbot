from typing import List, Dict
import hnswlib
import cohere
from cohere_config import co
import json


class Documents:
    """
    A class representing a collection of documents.
    ...

    Parameters:
    json_path (str): The file path to the JSON file containing the sources of the documents.
    ...

    Methods:
    ...
    """

    def __init__(self, json_path: str):
        self.docs = []
        self.docs_embs = []
        self.retrieve_top_k = 2
        self.rerank_top_k = 3
        self.sources = self.load_sources(json_path)  # Load sources from the JSON file
        self.load()  # Load documents from the sources
        self.embed()  # Embed the documents
        self.index()  # Index the documents

    def load_sources(self, json_path: str) -> List[Dict[str, str]]:
        """
        Loads the sources from the given JSON file.

        Parameters:
        json_path (str): The file path to the JSON file containing the sources of the documents.

        Returns:
        List[Dict[str, str]]: A list of dictionaries representing the sources of the documents.
        """
        with open(json_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def load(self) -> None:
        """
        Loads the documents from the sources.
        """
        print("Loading documents...")

        for source in self.sources:
            with open(source['file_path'], 'r', encoding='utf-8') as file:
                content = file.read()
                self.docs.append({
                    "title": source["title"],
                    "text": content,
                    "file_path": source["file_path"],  # Replace 'url' with 'file_path'
                })

    def embed(self) -> None:
        """
        Embeds the documents using the Cohere API.
        """
        print("Embedding documents...")

        batch_size = 90
        self.docs_len = len(self.docs)

        for i in range(0, self.docs_len, batch_size):
            batch = self.docs[i: min(i + batch_size, self.docs_len)]
            texts = [item["text"] for item in batch]
            docs_embs_batch = co.embed(
                texts=texts, model="embed-english-v3.0", input_type="search_document"
            ).embeddings
            self.docs_embs.extend(docs_embs_batch)

    def index(self) -> None:
        """
        Indexes the documents for efficient retrieval.
        """
        print("Indexing documents...")

        self.idx = hnswlib.Index(space="ip", dim=1024)
        self.idx.init_index(max_elements=self.docs_len, ef_construction=512, M=64)
        self.idx.add_items(self.docs_embs, list(range(len(self.docs_embs))))

        print(f"Indexing complete with {self.idx.get_current_count()} documents.")

    def retrieve(self, query: str, top_k=None) -> List[Dict[str, str]]:
        """
        Retrieves documents based on the given query.

        Parameters:
        query (str): The query to retrieve documents for.

        Returns:
        List[Dict[str, str]]: A list of dictionaries representing the retrieved documents, with 'title', 'text', and 'file_path' keys.
        """
        docs_retrieved = []
        query_emb = co.embed(
            texts=[query], model="embed-english-v3.0", input_type="search_query"
        ).embeddings

        # Get the IDs of the documents that are most similar to the query
        doc_ids = self.idx.knn_query(query_emb, k=(top_k or self.retrieve_top_k))[0][0]

        # You may want to rerank the retrieved documents for relevance
        docs_to_rerank = [self.docs[doc_id]["text"] for doc_id in doc_ids]

        rerank_results = co.rerank(
            query=query,
            documents=docs_to_rerank,
            top_n=self.rerank_top_k,
            model="rerank-english-v2.0",
        )

        # Extract the IDs of the top reranked documents
        doc_ids_reranked = [doc_ids[result.index] for result in rerank_results.results]

        # Create a list of dictionaries for the retrieved documents
        for doc_id in doc_ids_reranked:
            docs_retrieved.append(
                {
                    "title": self.docs[doc_id]["title"],
                    "text": self.docs[doc_id]["text"],
                    "file_path": self.docs[doc_id]["file_path"],
                }
            )
        return docs_retrieved
