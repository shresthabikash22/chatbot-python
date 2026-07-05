"""
Project: ELLIE - Virtual Friend Chatbot
Course: Advanced Artificial Intelligence
Author: Bikash Shrestha

Description:
This program creates a simple chatbot named ELLIE using the ChatterBot
library. The chatbot is trained using a custom YAML conversation file
and responds to user input until the user exits the program.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def create_chatbot():
    """
    Create and return the chatbot instance.
    """
    return ChatBot("ELLIE")


def train_chatbot(chatbot):
    """
    Train the chatbot using the custom conversation dataset.
    """
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("./data/conversation-data.yml")


def chat(chatbot):
    """
    Start the conversation with the chatbot.
    Type 'bye' to end the conversation.
    """
    print("ELLIE: Hello! I'm ELLIE, your virtual friend.")
    print("Type 'bye' anytime to exit.\n")

    while True:
        try:
            user_input = input("You: ")

            # Exit if the user types 'bye'
            if user_input.lower() == "bye":
                print("ELLIE: Goodbye! Have a wonderful day.")
                break

            response = chatbot.get_response(user_input)
            print("ELLIE:", response)

        except KeyboardInterrupt:
            print("\nELLIE: Goodbye!")
            break


def main():
    """
    Main function to create, train, and start the chatbot.
    """
    chatbot = create_chatbot()
    train_chatbot(chatbot)
    chat(chatbot)


if __name__ == "__main__":
    main()