from itertools import chain, repeat

import numpy as np
import pytest

from eps_entropy.entropy import *
from eps_entropy.symbols import *


def brownian(n):
    return np.cumsum(np.random.normal(size=n))


def words(word_length, repeats):
    symbol_sequence = "abcd"
    symbol_sequence = chain.from_iterable(repeat(symbol_sequence, repeats))
    words = n_pairs(symbol_sequence, word_length)
    return words


@pytest.mark.parametrize("method", ["numpy", "counter"])
def bench_count(benchmark, method):

    def setup():
        repeats = 100_000
        word_length = 10
        kw = {"method": method}
        if method == "numpy":
            kw["needs_translate"] = True
        return (words(word_length, repeats),), kw

    benchmark.pedantic(count, setup=setup, rounds=10)



def bench_exit_time_encoding(benchmark):

    size = 10_000
    eps = 1
    ts = brownian(size)

    benchmark(exit_time_encoding, ts, eps)
