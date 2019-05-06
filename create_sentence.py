from random import randint


def choose_random_word(d: dict) -> str:
    """Return a random word from a given dictionary <d> where the sum of all the
    values of <d> are <size>, and the probability of choosing a certain word is
    the value of <d>/<size>

    >>> d = {'hello': 1, 'world': 1, 'pineapple': 3}
    >>> choose_random_word(d) in ['hello', 'world', 'pineapple']
    True
    """
    size = 0
    for word in d:
        size += d[word]

    r = randint(1, size)
    total = 0
    chosen_word = list(d.keys())[0]
    for word in d:
        if total <= r < total + d[word]:
            chosen_word = word
            break
        else:
            total += d[word]

    return chosen_word


def create_sentence(first_words: dict, follower_words: dict) -> str:
    """Return a sentence

    >>> first_words = {'hello': 3}
    >>> follower_words = {'hello': {'#world': 3}, '#world': {None: 3}}
    >>> create_sentence(first_words, follower_words)
    'Hello #world'
    """
    words_for_sentence = []
    new_word = choose_random_word(first_words)

    while new_word is not None:
        words_for_sentence.append(new_word)
        new_word = choose_random_word(follower_words[new_word])

    sentence = ''
    for word in words_for_sentence:
        sentence += word + ' '

    return sentence[:-1].capitalize()

