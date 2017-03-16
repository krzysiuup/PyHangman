class Player:
    def __init__(self):
        self.chancesLeft = 11
        self.guess = str()
        self.rememberedLetters = set([""])

    def makeGuess(self):
        self.guess = input("Litera/Rozwiązanie: ")
        return self.guess

    def rememberLetter(self, letter):
        self.rememberedLetters.add(letter)

    def lostChance(self):
        self.chancesLeft -= 1

    def hasLost(self):
        return self.chancesLeft == 0
