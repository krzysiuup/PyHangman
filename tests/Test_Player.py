from src.Player import Player
import unittest

class Test_Player(unittest.TestCase):
    def test_lostChance_methodIsCalled_shouldDecrementChancesCounter(self):
        player = Player()
        player.lostChance()
        self.assertEqual(player.chancesLeft, 10)

    def test_hasLost_chanchesCounterIsSetToZero_shouldReturnTrue(self):
        player = Player()
        player.chancesLeft = 0
        self.assertTrue(player.hasLost())

    def test_hasLost_chancesCounterIsSetToOne_shouldReturnFalse(self):
        player = Player()
        player.chancesLeft = 1
        self.assertFalse(player.hasLost())

    def test_rememberLetter_theSameCharIsGivenTwice_charShouldBeAddedToSetOnce(self):
        player = Player()
        for i in range(2):
            player.rememberLetter("a")
        self.assertEqual(player.rememberedLetters, set(["", "a"]))

if __name__ == '__main__':
    unittest.main()
