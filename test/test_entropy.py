import pytest

from eps_entropy.entropy import *

def tupleize(x):
    return [tuple(i) for i in x]

def test_n_pairs():
    symbol_sequence = "abcd"
    target_words = list(symbol_sequence), ["ab", "bc", "cd"], ["abc", "bcd"], [symbol_sequence]

    for target in target_words:
        word_length = len(target[0])
        assert target == list(n_pairs(symbol_sequence, word_length, yield_string=True))
        if word_length > 1:
            assert tupleize(target) == list(n_pairs(symbol_sequence, word_length))
        else:
            assert target == list(n_pairs(symbol_sequence, word_length))


def test_translate():
    assert list(translate("abca")) == [0, 1, 2, 0]


def test_count_vals():
    lst = [1, 2, 2, 3, 3, 3]
    assert set(count(lst)) == set(lst)
    assert set(count(lst, method="numpy", needs_translate=True)) == set(lst)


@pytest.mark.parametrize("word_length, kw", [
    (1, {}),
    (5, {}),
    (1, {"count_method": "numpy", "needs_translate": True}),
    (5, {"count_method": "numpy", "needs_translate": True}),
])
def test_entropy(word_length, kw):
    lst = "aaaaaaa"
    assert 0 == entropy(lst, word_length, **kw)
