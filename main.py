from src.documents import Documents  # Adjust the import path if you're not using a src directory
from src.chatbot import MuseumChatbot  # Adjust as needed
from src.app import App
from cohere_config import co


def main():
    json_path = 'sources.json'
    documents = Documents(json_path)
    chatbot = MuseumChatbot(co, documents)
    # Create an instance of the App class with the Chatbot instance
    app = App(chatbot)

    # Run the chatbot
    app.run()

    # Run your chatbot or any other application logic


if __name__ == "__main__":
    main()
