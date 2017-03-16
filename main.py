from src.Sentence import Sentence
from src.Player import Player
from os import system

def isLetter(guess):
    return len(guess) == 1

def isSentence(guess):
    return len(guess) > 1

if __name__ == '__main__':
    sentence = Sentence()
    coveredSentence = sentence.cover()
    player = Player()
    inputWarning = ""

    while True:
        system('cls')

        print(coveredSentence)
        print("Pozostało {} szans.".format(player.chancesLeft))

        if player.hasLost():
            print("Przegrana")
            system('pause')
            break
        elif coveredSentence.isGuessed():
            print("Wygrana")
            system('pause')
            break

        print(inputWarning)
        guess = player.makeGuess()
        inputWarning = ""

        if isLetter(guess):
            if guess not in player.rememberedLetters:
                if sentence.isLetterOccurrs(guess):
                    coveredSentence.uncoverLetter(guess)
                else:
                    player.lostChance()
            player.rememberLetter(guess)
        elif isSentence(guess):
            if guess.lower() == sentence.content.lower():
                coveredSentence.uncoverSentence()
            else:
                player.lostChance()
        else:
            inputWarning = "Musisz wpisać twój wybór!"
