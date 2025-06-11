"""
tst.py

Ternary Search Tree implementation in Python.
Can be used for efficient word storage, lookup, and prefix-based autocomplete.
"""

from typing import Optional, List


class TSTNode:
    """
    Represents a node in a Ternary Search Tree (TST).

    Each node stores a single character and has up to three child nodes:
      - left: points to nodes with characters less than this node's character.
      - eq: points to nodes with the next character in the string (i.e., equal character).
      - right: points to nodes with characters greater than this node's character.

    Attributes:
        char (str): The character stored in this node.
        is_end_of_string (bool): Flag indicating whether this node marks the end of a valid string.
        left (Optional[TSTNode]): Left child node (less than `char`).
        eq (Optional[TSTNode]): Middle child node (equal to `char`).
        right (Optional[TSTNode]): Right child node (greater than `char`).
    """

    def __init__(self, char: str):
        self.char: str = char
        self.is_end_of_string: bool = False
        self.left: Optional["TSTNode"] = None
        self.eq: Optional["TSTNode"] = None
        self.right: Optional["TSTNode"] = None


class TernarySearchTree:
    """
    Ternary Search Tree with insert, search, and autocomplete methods.
    """

    def __init__(self):
        self.root: Optional[TSTNode] = None

    def insert(self, word: str) -> None:
        """Insert a word into the TST."""
        if word:
            self.root = self._insert(self.root, word, 0)

    def _insert(self, node: Optional[TSTNode], word: str, index: int) -> TSTNode:
        char = word[index]

        if node is None:
            node = TSTNode(char)

        if char < node.char:
            node.left = self._insert(node.left, word, index)
        elif char > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 < len(word):
                node.eq = self._insert(node.eq, word, index + 1)
            else:
                node.is_end_of_string = True

        return node

    def search(self, word: str) -> bool:
        """Search for a full word in the TST."""
        return self._search(self.root, word, 0)

    def _search(self, node: Optional[TSTNode], word: str, index: int) -> bool:
        if node is None or not word:
            return False

        char = word[index]

        if char < node.char:
            return self._search(node.left, word, index)
        elif char > node.char:
            return self._search(node.right, word, index)
        else:
            if index == len(word) - 1:
                return node.is_end_of_string
            return self._search(node.eq, word, index + 1)

    def autocomplete(self, prefix: str) -> List[str]:
        """
        Return all words in the TST that start with the given prefix.
        """
        results: List[str] = []
        node = self._get_node(self.root, prefix, 0)
        if node:
            if node.is_end_of_string:
                results.append(prefix)
            self._collect(node.eq, prefix, results)
        return results

    def _get_node(
        self, node: Optional[TSTNode], prefix: str, index: int
    ) -> Optional[TSTNode]:
        if not node or not prefix:
            return None

        char = prefix[index]

        if char < node.char:
            return self._get_node(node.left, prefix, index)
        elif char > node.char:
            return self._get_node(node.right, prefix, index)
        else:
            if index == len(prefix) - 1:
                return node
            return self._get_node(node.eq, prefix, index + 1)

    def _collect(
        self, node: Optional[TSTNode], prefix: str, results: List[str]
    ) -> None:
        if node:
            self._collect(node.left, prefix, results)

            if node.is_end_of_string:
                results.append(prefix + node.char)

            self._collect(node.eq, prefix + node.char, results)
            self._collect(node.right, prefix, results)
