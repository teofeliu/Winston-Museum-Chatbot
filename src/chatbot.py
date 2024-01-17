from typing import List, Dict
import cohere  # Make sure you have the Cohere SDK installed
from documents import Documents  # Your implementation of the Documents class
import hnswlib
from cohere_config import co  # Make sure you have a file with your Cohere configuration
import uuid

from looking_at import LookingAt
from models.classifier import Classifier
from models.cohere_model import CohereModel
from navigation.directions import Directions


class MuseumChatbot:
    def __init__(self, cohere_api_key: str, documents: Documents):
        self.classifier = Classifier()
        self.main_model = CohereModel(documents)
        self.directions = Directions(self.main_model)
        self.looking_at = LookingAt(self.main_model)
        self.cohere_client = cohere.Client(cohere_api_key)
        self.docs = documents
        self.conversation_id = str(uuid.uuid4())

    def generate_response(self, query: str):
        """
        Generates a response to the user's message.

        Parameters:
        query (str): The user's message.

        Yields:
        Event: A response event generated by the chatbot.

        Returns:
        List[Dict[str, str]]: A list of dictionaries representing the retrieved documents.

        """
        category = self.classifier.classify(query)
        print("Category: " + category)
        if category == "directions":
            yield from self.directions.handle_directions_query(query)
        elif category == "looking at":
            yield from self.looking_at.handle_looking_at_query(query)
        elif category == "chat":
            yield from self.main_model.chat(query)


    def retrieve_docs(self, response, top_k=0) -> List[Dict[str, str]]:
        """
        Retrieves documents based on the search queries in the response.

        Parameters:
        response: The response object containing search queries.

        Returns:
        List[Dict[str, str]]: A list of dictionaries representing the retrieved documents.

        """
        # Get the query(s)
        queries = []
        for search_query in response.search_queries:
            queries.append(search_query["text"])

        # Retrieve documents for each query
        retrieved_docs = []
        for query in queries:
            retrieved_docs.extend(self.docs.retrieve(query, 1))

        # # Uncomment this code block to display the chatbot's retrieved documents
        # print("DOCUMENTS RETRIEVED:")
        # for idx, doc in enumerate(retrieved_docs):
        #     print(f"doc_{idx}: {doc}")
        # print("\n")

        return retrieved_docs