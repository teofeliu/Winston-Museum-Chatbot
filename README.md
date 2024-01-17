# Winston: The Guggenheim Museum's Interactive Chatbot Guide

## Introduction

This project presents a RAG (Retrieval Augmented Generation)-powered chatbot system designed to enhance the experience of museum visitors. The chatbot plays Winston, an interactive tour guide designed to guide visitors through Bilbao's Guggenheim Museum. Capable of discussing various artworks, Winston also provides directional assistance to specific pieces upon request. Winston knows when to fetch directions, utilize the user's current position and orientation, and fetch internal documents in order to satisfy any needs a museum visitor might have.

## Overview

Winston integrates a few of Cohere's LLMs to effectively handle diverse user inquiries. From general information about the museum's collection to navigational support and in-depth details about specific artworks, Winston is equipped to respond accurately and efficiently.

### Key Features

- **Directional Assistance**: Offers guidance and directions to artworks based on visitor queries, including recommended pieces.
- **Artwork Insights**: Provides enriched information about artworks, utilizing positional data for contextual relevance.
- **Efficient Document Retrieval**: Accesses a comprehensive set of documents for more detailed information about the museum's exhibits.
- **Avoid Hallucinations**: Winston is aware of the collection's artwork information and will only return true results relevant to the museum.

### Streamlined Query Handling

Designed with a focus on responsiveness, Winston handles a wide range of queries, prioritizing quick information delivery while seamlessly managing more complex requests for API-based information retrieval.

### Advanced Interaction Design

Winston's multi-step response generation demonstrates its ability to deliver comprehensive and contextually appropriate answers, illustrating its sophisticated interaction capabilities.

## Technologies Used

- **Cohere's Chatbot and Classifier**: Powers the natural language understanding and response generation.
- **Custom APIs**: Integrated for navigational and detailed artwork information.
- **Python**: The foundational programming language for the project.

## Conclusion

Winston exemplifies the application of AI in enhancing cultural experiences. Its role in the Guggenheim Museum demonstrates a smart use of technology to make art more accessible and engaging, reflecting a modern approach to museum interaction.
