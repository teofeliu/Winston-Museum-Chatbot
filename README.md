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


# Example

**User**: Introduce yourself.
**Winston**: Hello, my name is Winston and I will be your tour guide today at the Guggenheim Museum Bilbao. It's a pleasure to have you here and I'm excited to show you around this incredible museum. The Guggenheim Bilbao is a contemporary art museum located in the heart of the city and is one of the most iconic structures in Bilbao. It was designed by the renowned Canadian-American architect Frank Gehry and opened in 1997.

The museum is home to a remarkable collection of modern and contemporary art, including works by some of the world's most celebrated artists such as Pablo Picasso, Joan Miró, and Jeff Koons. As we tour the museum, we will have the opportunity to view some of these incredible works and learn more about the artists who created them.

I will also share with you the fascinating story of how the Guggenheim Bilbao came to be and how it has become an integral part of the city. Join me on this journey through art and architecture as we explore the many wonders that the Guggenheim Museum Bilbao has to offer. 

Are you ready to begin? 

**User**: Take me to your favorite Basquiat painting

**Winston**: We do have an artwork in the collection that is one of my favorites and very close to my heart -- that is "Moses and the Egyptians" by Jean-Michel Basquiat. 
This painting holds significant importance in Basquiat's career as it was created shortly after he was discovered as an artist, before his period of maximum productivity. It is essential for understanding the development of his painting style during the 1980s. 
"Moses and the Egyptians" depicts the profile of Moses through white lines in an impulsive manner, contrasting with the orderly inscriptions on the tablets of the law. The painting alludes to a biblical episode but can also be related to the history of Africa. 
If you would like to know more about this painting and see it with your own eyes, I would be delighted to take you there. To get there, you should head west on the main corridor, take a right at the large red statue, and then go straight for 8 steps. You will find "Moses and the Egyptians" to your right next to a group of smaller sculptures. 
I hope you enjoy your visit and appreciate this remarkable artwork! Would you like me to tell you more about Basquiat or other artworks in our collection?

**User**: Take me to a Picasso

**Winston**: Unfortunately, we don't seem to have any paintings by Picasso in our collection. However, we do have the Imaginary Portrait of Goya by Antonio Saura. While it may not have been created by your favorite Picasso, it's a remarkable piece of art nonetheless. If you'd like to see it, simply follow the directions to the artwork that I'm about to give you.

**User**: My apologies, I thought I was currently looking at one. What painting is currently in front of me?

**Winston**: Ah, you're standing in front of The Matter of Time, a sculpture by Richard Serra. 
This sculpture is an incredible interactive piece, as the viewer is meant to walk through and around the different sections of toruses and spheres. The experience is designed to create an unforgettable, dizzying feeling of space in motion. 
Would you like to know more about the sculpture? Or perhaps the artist behind it?

**User**: I just moved to a different spot. Tell me about the artist behind this artwork.

**Winston**: The artist behind the work you're looking at is Antonio Saura. 
Saura was inspired by the work of two Spanish masters, Diego Velázquez and Francisco de Goya. He was particularly fascinated by The Dog, one of Goya's so-called Black Paintings preserved in Madrid's Museo Nacional del Prado. This inspired Saura to produce a series of paintings titled Imaginary Portrait of Goya (or Goya's Dog), which he worked on from 1957 until 1992. 
In the Guggenheim Museum Bilbao's Imaginary Portrait of Goya, darkness or the void occupies most of the composition, with only a small area of white in the upper right corner. According to Saura, this painting evokes notions of emergence, birth, and appearance, all states that correspond with those of artistic creation.

**User**: Great. Anything else you could recommend me? I'm not the biggest fan of abstract art.

**Winston**: Certainly. If you're not a fan of abstract art, I can recommend some artists who work with more representational forms, such as Cy Twombly and Willem de Kooning. 
Cy Twombly worked within the style of abstract expressionism but developed a signature style marked by graffiti-like scratches and scribbles, that nonetheless referenced and subverted the dominant painterly mode of the time. His work later took on more historical undertones, looking at the cruelty and madness of historical assassinations and the lives of classical literature and mythology. 
Willem de Kooning is another artist who has worked within and around abstract expressionism but who often drew from observable reality, particularly figures and landscapes. His famous Women series integrated the human form with aggressive paint application, bold colours, and sweeping strokes of abstract expressionism. Later, working on Long Island, his compositions became increasingly pastoral, yielding to a more restrained and clear form. 
While these artists may have worked within the tradition of abstract expressionism, the works themselves often contain more figurative elements, either referencing history or drawing from observable reality. Would you like to know more about any of these artists and their works?
