import hnswlib
import cohere
from cohere_config import co  # Make sure you have a file with your Cohere configuration
from src.chatbot import MuseumChatbot  # Adjust as needed


class App:
    def __init__(self, chatbot: MuseumChatbot):
        """
        Initializes an instance of the App class.

        Parameters:
        chatbot (Chatbot): An instance of the Chatbot class.

        """
        self.chatbot = chatbot

    def run(self):
        """
        Runs the chatbot application.

        """
        while True:
            # Get the user message
            message = input("User: ")

            # Typing "quit" ends the conversation
            if message.lower() == "quit":
                print("Ending chat.")
                break
            else:
                print(f"User: {message}")

            # Get the chatbot response
            response = self.chatbot.generate_response(message)

            # Print the chatbot response
            print("Chatbot:")
            flag = False
            for event in response:
                # Text
                if event.event_type == "text-generation":
                    print(event.text, end="")

                """
                # Citations
                if event.event_type == "citation-generation":
                    if not flag:
                        print("\n\nCITATIONS:")
                        flag = True
                    print(event.citations)
                """

            print(f"\n{'-' * 100}\n")