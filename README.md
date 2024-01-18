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





# Example Chatbot Interaction
**User**: Introduce yourself.

**Winston**: Hello, my name is Winston and I will be your tour guide today at the Guggenheim Museum Bilbao. It's a pleasure to have you here and I'm excited to show you around this incredible museum. The Guggenheim Bilbao is a contemporary art museum located in the heart of the city and is one of the most iconic structures in Bilbao. It was designed by the renowned Canadian-American architect Frank Gehry and opened in 1997.

**User**: Take me to your favorite Basquiat painting.

**Winston**: We do have an artwork in the collection that is one of my favorites and very close to my heart -- that is "Moses and the Egyptians" by Jean-Michel Basquiat. To get there, you should head west on the main corridor, take a right at the large red statue, and then go straight for 8 steps. You will find "Moses and the Egyptians" to your right next to a group of smaller sculptures.

**User**: Take me to a Picasso.

**Winston**: Unfortunately, we don't seem to have any paintings by Picasso in our collection. However, we do have the Imaginary Portrait of Goya by Antonio Saura. While it may not have been created by your favourite Picasso, it's a remarkable piece of art nonetheless. If you'd like to see it, simply follow the directions to the artwork that I'm about to give you.

**User**: My apologies, I thought I was currently looking at one. What painting is currently in front of me?

**Winston**: Ah, you're standing in front of The Matter of Time, a sculpture by Richard Serra...

**User**: I just moved to a different spot. Tell me about the artist behind this artwork.

**Winston**: The artist behind the work you're looking at is Antonio Saura...

**User**: Great. Anything else you could recommend me? I'm not the biggest fan of abstract art.

**Winston**: Certainly. If you're not a fan of abstract art, I can recommend some artists who work with more representational forms, such as Cy Twombly and Willem de Kooning...
