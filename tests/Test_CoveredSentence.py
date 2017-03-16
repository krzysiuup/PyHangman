import unittest
from src.CoveredSentence import CoveredSentence

class Test_CoveredSentence(unittest.TestCase):
    def test_replaceLettersWithDashes_sentenceIsGiven_shouldReplaceAllLettersWithDashes(self):
        covered = CoveredSentence("Jak Kuba Bogu, tak Bóg Kubie.")
        expected = "--- ---- ----, --- --- -----."
        self.assertEqual(covered.content, expected)

    def test_uncoverLetter_nothingIsGiven_shouldNotUncoverAnyLetter(self):
        covered = CoveredSentence("Jak Kuba Bogu, tak Bóg Kubie.")
        covered.uncoverLetter("")
        expected = "--- ---- ----, --- --- -----."
        self.assertEqual(covered.content, expected)

    def test_uncoverLetter_occurringLetterIsGivenInLowercase_shouldUncoverAllGivenLetterOccurrences(self):
        covered = CoveredSentence("Jak Kuba Bogu, tak Bóg Kubie.")
        covered.uncoverLetter("k")
        expected = "--k K--- ----, --k --- K----."
        self.assertEqual(covered.content, expected)

    def test_uncoverLetter_occurringLetterIsGivenInUppercase_shouldUncoverAllGivenLetterOccurrences(self):
        covered = CoveredSentence("Jak Kuba Bogu, tak Bóg Kubie.")
        covered.uncoverLetter("K")
        expected = "--k K--- ----, --k --- K----."
        self.assertEqual(covered.content, expected)


if __name__ == '__main__':
    unittest.main()
