from random import randint
from .CoveredSentence import CoveredSentence

class Sentence:
    def __init__(self, content=None):
        # NOTE: Probably unpythonic constructor overloading. I probably should use isinstance, but it's no time to think about it.
        if content == None:
            self.content = self._getRandom()
        else:
            self.content = content

    def _getRandom(self):
        with open("sentences.txt") as sentencesFile:
            sentences = sentencesFile.read().split("\n")
            randomIndex = randint(0, len(sentences))
            return sentences[randomIndex]

    def isLetterOccurrs(self, givenLetter):
        return givenLetter.lower() in self.content.lower()

    def cover(self):
        return CoveredSentence(self)

    def __str__(self):
        return self.content
