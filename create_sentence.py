from random import randint


def choose_random_word(d: dict) -> str:
    """Return a random word from a given dictionary <d> where the odds of
    picking any word is the value of <d> at word over the sum off all values.
    ( P(word) = d[word] / sum(d.values()) )

    >>> d = {'hello': 1, 'world': 2, 'pineapple': 1}
    >>> choose_random_word(d) in ['hello', 'world', 'pineapple']
    True
    """
    size = sum(d.values())

    r = randint(0, size)
    total = 0
    for word, val in d.items():
        total += val
        if r <= total:
            return word


def create_sentence(first_words: dict, follower_words: dict) -> str:
    """Return a sentence

    >>> first_words = {'hello': 3}
    >>> follower_words = {'hello': {'#world': 3}, '#world': {None: 3}}
    >>> create_sentence(first_words, follower_words)
    'Hello #world'
    """
    new_word = choose_random_word(first_words)
    sentence = ''

    while new_word is not None:
        sentence += new_word + ' '
        new_word = choose_random_word(follower_words[new_word])

    return sentence[:-1].capitalize()       # Remove extra space and capitalize
