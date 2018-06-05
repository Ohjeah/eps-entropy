import pytest

from eps_entropy.symbols import *

@pytest.mark.parametrize("number, target", [
    (0, 0),
    (-0.3, -1),
    (0.7, 1)
])
def test_wrapping_int(number, target):
    assert wrapping_int(number) == target


def test_eps_grid():
    ts = np.arange(10, dtype=float)
    eps = 0.1

    symbols = eps_grid(ts, eps, offset="zero")
    np.testing.assert_allclose(symbols, ts / eps)

    symbols = eps_grid(ts, eps, offset="mean")
    np.testing.assert_allclose(symbols, (ts - ts.mean()) / eps)

    assert [] == eps_grid([], 1)


def test_exit_times_symbols():
    ts = np.array([0, 1, 2, 3, 4])
    eps = 1
    tau = 1

    symbols = exit_times_symbols(ts, eps, tau)
    times, up_down = map(list, zip(*symbols))

    assert times == [1, 1, 1, 1]
    assert up_down == [1, 1, 1, 1]
