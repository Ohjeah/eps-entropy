import numpy as np

from .utils import find


def wrapping_int(x):
    sign = np.sign(x)
    return int(sign * np.ceil(np.abs(x)))


def eps_grid(ts, eps, offset="mean", return_dtype=np.int):
    if len(ts) == 0:
        return []

    if offset == "mean":
        ts0 = np.mean(ts)
    elif offset == "zero":
        ts0 = ts[0]
    else:
        ts0 = offset
    ts = ts - ts0


    low = wrapping_int(np.min(ts) / eps)
    high = wrapping_int(np.max(ts) / eps)

    ts_ = ts/eps
    symbols = np.zeros_like(ts)
    for s in range(low, high + 1):
        symbols = np.where(np.logical_and(s <= ts_, ts_ < s + 1), s, symbols)
    return np.array(symbols, dtype=return_dtype)


def exit_time_encoding(signal, eps):
    """
    Calculate the exit times out of the interval of size epsilon centered at the starting value.

    Arguments:
        signal: numpy array holding a time series
        eps: interval size for exit time calculation

    Returns:
        times: (np.array) exit times
        up_down: (list) list of up and down markers
    """
    times = []
    up_down = []
    while len(signal) > 1:
        try:
            # find is a generator so that we dont look into the whole signal at once
            # it is equivalent to first_out = np.nonzero(np.abs(signal - signal[0])[1:] > eps/2.)[0][0]
            first_out = next(find(signal, lambda x: np.abs(x - signal[0]) > eps/2., chunk_size=128))[0][0]
            k = wrapping_int((signal[first_out] - signal[0]) / eps)
            signal = signal[first_out:]
            times.append(first_out)
            up_down.append(k)
        except StopIteration:   # when the threshold is never or not anymore reached
            break
    return np.array(times), up_down


def exit_times_symbols(ts, eps, tau):
    times, up_down = exit_time_encoding(ts, eps)
    times = eps_grid(times, tau, offset=0)
    return list(zip(times, up_down))
