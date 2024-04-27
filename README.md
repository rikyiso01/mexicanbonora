# MexicanBonora

Telegram chat bot that only replies in Spanish

## Description

- When the bot receives a text input the text is translated into English by using one of the
  translators available in the [translators library](https://pypi.org/project/translators/)

- A reply is generated using the [chatterbot library](https://pypi.org/project/ChatterBot/)

- The chatterbot model is trained during the docker container build by using
  the [chatterbot corpus](https://pypi.org/project/chatterbot-corpus/)

- The reply is then translated using into Spanish
