from __future__ import annotations
import collections.abc

from mexicanbonora.chat import CHATBOT

collections.Hashable = collections.abc.Hashable
from chatterbot.trainers import ChatterBotCorpusTrainer


def train():
    trainer = ChatterBotCorpusTrainer(CHATBOT)
    trainer.train("chatterbot.corpus.english")


if __name__ == "__main__":
    train()
