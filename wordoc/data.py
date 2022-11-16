import os


words = list()
word_length = 5
dictionary = set()

DICT_PATHS = [
    'wordoc/en_US.dic',
    '/home/shonku/wordoc/wordoc/en_US.dic'
]

POPULAR_PATHS = [
    'wordoc/popular.txt',
    '/home/shonku/wordoc/wordoc/popular.txt'
]


DICT_PATH = DICT_PATHS[0]
if not os.path.exists(DICT_PATH): DICT_PATH = DICT_PATHS[1]

POPULAR_PATH = POPULAR_PATHS[0]
if not os.path.exists(POPULAR_PATH): POPULAR_PATH = POPULAR_PATHS[1]


def load_words():
    if len(words) > 0: return

    with open(DICT_PATH) as words_file:
        for line in words_file:
            word = line.strip()

            if word.find('/') > 0:
                word = word[:word.find('/')]
                
            word = word.upper()
            if word.isalpha() and len(word) == word_length:
                dictionary.add(word)
    print(f'Dictionary {len(dictionary)} words')

    with open(POPULAR_PATH) as words_file:
        for line in words_file:
            word = line.strip()
            word = word.upper()
            if word.isalpha() and len(word) == word_length and len(set(word)) == word_length and (word in dictionary):
                words.append(word)
    print(f'Popular {len(words)} words')


def get_words():
    if len(words) == 0:
        raise Exception("Words not loaded")
    return words


def exists(word):
    return word in dictionary