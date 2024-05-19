import json

def get_word(dictionary_word):
    """
    Extracts the word from a dictionary entry.

    Parameters:
        dictionary_word (str): The dictionary entry containing the word, pronunciation, and definition.

    Returns:
        str: The extracted word from the dictionary entry.
    """
    start = dictionary_word.find("@")
    end = dictionary_word.find("\n") if dictionary_word.find(" /") == -1 else dictionary_word.find(" /")
    word = dictionary_word[start+1:end]
    return word

def get_pronunciation(dictionary_word):
    """
    Extracts the pronunciation from a dictionary entry.

    Parameters:
        dictionary_word (str): The dictionary entry containing the word, pronunciation, and definition.

    Returns:
        str: The extracted pronunciation from the dictionary entry. Returns an empty string if no pronunciation is found.
    """
    start = dictionary_word.find(' /')
    if start == -1: return ""
    end = dictionary_word.find("\n")
    pronunciation = dictionary_word[start+2:end-1]
    return pronunciation

def get_definition(dictionary_word):
    """
    Extracts the definition from a dictionary entry.

    Parameters:
        dictionary_word (str): The dictionary entry containing the word, pronunciation, and definition.

    Returns:
        str: The extracted definition from the dictionary entry.
    """
    start = dictionary_word.find("\n")
    end = len(dictionary_word)
    definition = dictionary_word[start+1:end]
    return definition

def analyze(dictionary_word):
    """
    Analyzes a dictionary entry and extracts the word, pronunciation, and definition.

    Parameters:
        dictionary_word (str): The dictionary entry to be analyzed.

    Returns:
        dict: A dictionary containing the word, pronunciation, and definition.
    """
    data ={
        'word':get_word(dictionary_word),
        'pronunciation':get_pronunciation(dictionary_word),
        'definition':get_definition(dictionary_word)
    }
    dictionary = dict()
    for key, value in data.items():
        dictionary[key] = value
    return dictionary

def create_database(content, start=0, end=1):
    """
    Creates a database of dictionary entries from a given content string.

    Parameters:
        content (str): The content string containing multiple dictionary entries.
        start (int, optional): The starting index for parsing. Defaults to 0.
        end (int, optional): The ending index for parsing. Defaults to 1.

    Returns:
        list: A list of dictionaries, each containing the word, pronunciation, and definition of a dictionary entry.
    """
    dictionary = list()
    while True:
        start = content.find("@",start)
        end = content.find("\n@",start+1)
        if end == -1 or start == -1 or end < 0:
            break
        dictionary_word = content[start:end]
        dictionary.append(analyze(dictionary_word))
        start = end
    end = len(content)
    dictionary_word = content[start:end]
    dictionary.append(analyze(dictionary_word))
    return dictionary

with open("./database/anhviet109K.txt", 'r', encoding = 'utf-8') as file: 
    content = file.read()
    dictionary = create_database(content)
    with open("./database/dba-v.json",'w', encoding = 'utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False)

with open("./database/vietanh.txt", 'r', encoding = 'utf-8') as file: 
    content = file.read()
    dictionary = create_database(content)
    with open("./database/dbv-a.json",'w', encoding = 'utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False)