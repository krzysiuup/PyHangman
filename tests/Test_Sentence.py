from src.Sentence import Sentence
from src.CoveredSentence import CoveredSentence
import unittest

class Test_Sentence(unittest.TestCase):
    def test_occurringLetterIsGivenInLowercase_shouldReturnTrue(self):
        sentence = Sentence("Jak Kuba Bogu, tak Bóg Kubie.")
        self.assertTrue(sentence.isLetterOccurrs("k"))

    def test_occurringLetterIsGivenInUppercase_shouldReturnTrue(self):
        sentence = Sentence("Jak Kuba Bogu, tak Bóg Kubie.")
        self.assertTrue(sentence.isLetterOccurrs("K"))

    def test_cover_shouldReturnCoveredSentenceObject(self):
        sentence = Sentence("Jak Kuba Bogu, tak Bóg Kubie.")
        coveredSentence= sentence.cover()
        self.assertTrue(isinstance(coveredSentence, CoveredSentence))

if __name__ == '__main__':
    unittest.main()
