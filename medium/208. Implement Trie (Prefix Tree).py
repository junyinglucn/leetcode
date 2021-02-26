# Solution A
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.l.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.l

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        length = len(prefix)
        for w in self.l:
            if w[:length] == prefix:
                return True
        return False
