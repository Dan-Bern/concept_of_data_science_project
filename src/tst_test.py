import os
import unittest
from tst import TernarySearchTree


def load_words_from_file(relative_path: str) -> list[str]:
    """Helper function to load words from a file relative to this test file, one per line.
    
    Returns:
        list[str]: A list of non-empty stripped lines.
    """
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, relative_path)
    with open(filepath, "r") as file:
        return [line.strip() for line in file if line.strip()]


class TestTernarySearchTree(unittest.TestCase):
    """
    Unit tests for the TernarySearchTree class.
    """
    def setUp(self):
        """
        Set up test environment with a populated TST and test word lists.
        """
        self.tst = TernarySearchTree()
        self.words = load_words_from_file(os.path.join("data", "insert_words.txt"))
        self.non_existing = load_words_from_file(
            os.path.join("data", "not_insert_words.txt")
        )

        for word in self.words:    # Insert test words into the tree
            self.tst.insert(word)

    def test_insert_and_search_existing_words(self):
        for word in self.words:
            self.assertTrue(self.tst.search(word), f"Word '{word}' should be found.")

    def test_search_non_existing_words(self):
        """
        Ensure that non-inserted words are not found in the TST.
        """
        for word in self.non_existing:
            self.assertFalse(
                self.tst.search(word), f"Word '{word}' should NOT be found."
            )

    def test_insert_duplicate_word(self):
        """
        Inserting a duplicate word should not affect its retrievability.
        """
        word = self.words[0] if self.words else "apple"
        self.tst.insert(word)
        self.assertTrue(self.tst.search(word))

    def test_empty_string_handling(self):
        """
        Searching for an empty string should always return False.
        """
        self.assertFalse(self.tst.search(""), "Empty string should not be found.")

    def test_autocomplete_basic(self):
        """
        Test autocomplete results for common prefixes.
        """
        if "banana" in self.words:
            expected = [w for w in self.words if w.startswith("ba")]
            self.assertCountEqual(self.tst.autocomplete("ba"), expected)
        if "app" in self.words:
            expected = [w for w in self.words if w.startswith("app")]
            self.assertCountEqual(self.tst.autocomplete("app"), expected)

    def test_autocomplete_no_results(self):
        """
        Autocomplete on a non-existent prefix should return an empty list.
        """
        self.assertEqual(self.tst.autocomplete("zzz"), [])


if __name__ == "__main__":
    unittest.main()
