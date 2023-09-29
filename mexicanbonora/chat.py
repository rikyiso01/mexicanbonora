from __future__ import annotations
from chatterbot import ChatBot


CHATBOT = ChatBot("Mexican Bonora", read_only=True)


def chat(input: str) -> str:
    return CHATBOT.get_response(input)


def main():
    print("Ready")
    while True:
        print(chat(input("> ")))


if __name__ == "__main__":
    main()
