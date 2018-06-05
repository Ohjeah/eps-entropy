from collections import Counter
from itertools import tee, chain, repeat

import numpy as np
import scipy.stats


def n_pairs(symbol_sequence, n, yield_string=False):
    """Yields

    (x0, x1, x2, x3) -> (x0, ..., xn), (x1, ... xn+1), ...
    """
    if n > 1:
        s = tee(iter(symbol_sequence), n)
        for i in range(1, n):
            for _ in range(i):
                next(s[i], None)
        it = zip(*s)
    else:
        it = iter(symbol_sequence)
    if yield_string:
        it = map("".join, it)
    yield from it


def convert(words):
    yield from map(lambda x: "".join(map(str, x)), words)


def translate(words, tab=None):
    """Enumerates a collection of words.

    Each word will be translated into a integer.
    """
    tab = tab if isinstance(tab, dict) else {}
    i = 0
    for word in words:
        if word not in tab:
            tab[word] = i
            i += 1
        yield tab[word]


def count(words, method="counter", needs_translate=False):
    if needs_translate:
        words = translate(words)
    if method == "counter":
        return list(Counter(words).values())
    return np.bincount(np.fromiter(words, int))


def entropy(symbolic_sequence, word_length, convert_to_string=False, count_method="counter", needs_translate=False, base=None):
    words = n_pairs(symbolic_sequence, word_length)
    if convert_to_string or needs_translate:
        words = convert(words)
    return scipy.stats.entropy(count(words, method=count_method, needs_translate=needs_translate), base=base)
