class CoveredSentence:
    def __init__(self, sentence):
        self.original = str(sentence)
        self.content = self._replaceLettersWithDashes(str(self.original))

    def _replaceLettersWithDashes(self, sentenceToCover):
        result = str()
        for char in self.original:
            if char.isalpha():
                result += "-"
            else:
                result += char
        return result

    def uncoverLetter(self, givenLetter):
        contentList = list(self.content)
        for i in range(len(self.original)):
            if givenLetter.lower() == self.original[i].lower():
                contentList[i] = self.original[i]

        self.content = "".join(contentList)

    def uncoverSentence(self):
        self.content = self.original

    def isGuessed(self):
        return self.original == self.content

    def __str__(self):
        return self.content
