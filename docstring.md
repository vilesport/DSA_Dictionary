**Project DSA: Dictopedia documentations**
---

***Docstring***
---

**TRIE**
---

- `TrieNode` : A node in the Trie structure.       
  - Attributes:
    - child (dict): A dictionary mapping each character to its corresponding TrieNode.
    - EOW (bool): A boolean indicating if the node represents the end of a word.
    - data (list): A list storing additional data associated with the word ending at this node.
    - `__init__(self)`: Initializes a TrieNode with an empty child dictionary, EOW set to False, and an empty data list.
