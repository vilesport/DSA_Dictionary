**Project DSA: Dictopedia documentations**
---

***Docstring***
---

**TRIE**
---

- `TrieNode` : A node in the Trie structure.       
  - Attributes:
    - `child (dict)`: A dictionary mapping each character to its corresponding TrieNode.
    - `EOW (bool)`: A boolean indicating if the node represents the end of a word.
    - `data (list)`: A list storing additional data associated with the word ending at this node.
    - `__init__(self)`: Initializes a TrieNode with an empty child dictionary, EOW set to False, and an empty data list.

- `Trie`:  A Trie data structure for storing strings and their associated data.
  - `root (TrieNode)`: The root node of the Trie
  - `__init__(self)`: Initializes the Trie with a root TrieNode.
  - `insert(self, word, data)`: Inserts a word and its associated data into the Trie.
    - Args:
      - `word (str)`: The word to be inserted into the Trie.
      - `data (any)`: The data to be associated with the word. 
  - `search(self, word)`: Searches for a word in the Trie and returns its associated data.
    - Args:
      - `word (str)`: The word to search for in the Trie.
    - Returns:
      - `node.data (list)`: The data associated with the word if it exists, otherwise None.
