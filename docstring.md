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
    - Parameters:
      - `word (str)`: The word to be inserted into the Trie.
      - `data (any)`: The data to be associated with the word. 

  - `search(self, word)`: Searches for a word in the Trie and returns its associated data.
    - Parameters:
      - `word (str)`: The word to search for in the Trie.
    - Returns:
      - `node.data (list)`: The data associated with the word if it exists, otherwise None.

  - `suggest(self, node, prefix, num, current)`: Helper function to suggest words with a given prefix.
    - Parameters:
      - `node (TrieNode)`: The current TrieNode.
      - `prefix (str)`: The current prefix being formed.
      - `num (int)`: The maximum number of suggestions required.
      - `current (int)`: The current count of suggestions.
    - Returns:
      - `words (list)`: A list of tuples containing the suggested words and their associated data.

  - `autocomplete(self, prefix, num)`: Autocompletes words based on a given prefix.
    - Parameters:
      - `prefix (str)`: The prefix to autocomplete.
      - `num (int)`: The maximum number of autocompletions to return.
    - Returns:
      - `(list)`: A list of tuples containing the autocompleted words and their associated data.
---

**Load Database**
---

- `get_word(dictionary_word)`: Extracts the word from a dictionary entry.
  - Parameters:
    - `dictionary_word (str)`: The dictionary entry containing the word, pronunciation, and definition.
  - Returns:
    - `(str)`: The extracted word from the dictionary entry.


- `get_pronunciation(dictionary_word)`: Extracts the pronunciation from a dictionary entry.
  - Parameters:
    - `dictionary_word (str)`: The dictionary entry containing the word, pronunciation, and definition.
  - Returns:
    - `(str)`: The extracted pronunciation from the dictionary entry. Returns an empty string if no pronunciation is found.


- `get_definition(dictionary_word)`: Extracts the definition from a dictionary entry.
  - Parameters:
    - `dictionary_word (str)`: The dictionary entry containing the word, pronunciation, and definition.
  - Returns:
    - `(str)`: The extracted definition from the dictionary entry.
  - `analyze(dictionary_word)`: Analyzes a dictionary entry and extracts the word, pronunciation, and definition.
    - Parameters:
      - `dictionary_word (str)`: The dictionary entry to be analyzed.
    - Returns:
      - `(dict)`: A dictionary containing the word, pronunciation, and definition.


- `create_database(content, start=0, end=1)`: Creates a database of dictionary entries from a given content string.
  - Parameters:
    - `content (str)`: The content string containing multiple dictionary entries.
    - `start (int, optional)`: The starting index for parsing. Defaults to 0.
    - `end (int, optional)`: The ending index for parsing. Defaults to 1.
  - Returns:
    - `(list)`: A list of dictionaries, each containing the word, pronunciation, and definition of a dictionary entry.
