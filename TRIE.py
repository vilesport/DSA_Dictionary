class TrieNode:
    """
    A node in the Trie structure.

    Attributes:
        child (dict): A dictionary mapping each character to its corresponding TrieNode.
        EOW (bool): A boolean indicating if the node represents the end of a word.
        data (list): A list storing additional data associated with the word ending at this node.
    """

    def __init__(self):
        """
        Initializes a TrieNode with an empty child dictionary, EOW set to False, and an empty data list.
        """
        self.child = {}
        self.EOW = False
        self.data = []

class Trie:
    """
    A Trie data structure for storing strings and their associated data.

    Attributes:
        root (TrieNode): The root node of the Trie.
    """

    def __init__(self):
        """
        Initializes the Trie with a root TrieNode.
        """
        self.root = TrieNode()

    def insert(self, word, data):
        """
        Inserts a word and its associated data into the Trie.

        Args:
            word (str): The word to be inserted into the Trie.
            data (any): The data to be associated with the word.
        """
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.EOW = True
        node.data.append(data)

    def search(self, word):
        """
        Searches for a word in the Trie and returns its associated data.

        Args:
            word (str): The word to search for in the Trie.

        Returns:
            list: The data associated with the word if it exists, otherwise None.
        """
        node = self.root
        for char in word:
            if char not in node.child:
                return None
            node = node.child[char]
        if node.EOW:
            return node.data
        return None

    def suggest(self, node, prefix, num, current):
        """
        Helper function to suggest words with a given prefix.

        Args:
            node (TrieNode): The current TrieNode.
            prefix (str): The current prefix being formed.
            num (int): The maximum number of suggestions required.
            current (int): The current count of suggestions.

        Returns:
            list: A list of tuples containing the suggested words and their associated data.
        """
        words = []
        if node.EOW:
            words.extend((prefix, d) for d in node.data)
            current += len(words)
        for char, child in node.child.items():
            if current >= num:
                return words
            words.extend(self.suggest(child, prefix + char, num, current + len(words)))
        return words

    def autocomplete(self, prefix, num):
        """
        Autocompletes words based on a given prefix.

        Args:
            prefix (str): The prefix to autocomplete.
            num (int): The maximum number of autocompletions to return.

        Returns:
            list: A list of tuples containing the autocompleted words and their associated data.
        """
        node = self.root
        for char in prefix:
            if char not in node.child:
                return []
            node = node.child[char]
        return self.suggest(node, prefix, num, 0)[:num]