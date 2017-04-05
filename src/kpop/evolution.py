"""
General routines that simulation evolution.
"""
import numpy as np

from kpop.utils import fill_freqs_vector, flatten_frequencies


def frequency_drift_1D(freqs_vector, n_generations, size):
    """
    Simulate the genetic drift from a vector after the given number of
    generations.

    Args:
        freqs_vector: a 1D input vector of frequencies.
        n_generations: number of generations.
        size: effective size of population.
    """

    freqs_vector = np.array(freqs_vector)
    for _ in range(n_generations):
        for j, f in enumerate(freqs_vector):
            freqs_vector[j] = np.random.binomial(size, f) / size
    return freqs_vector


def frequency_drift(freqs, n_generations, size):
    """
    Simulate the genetic drift from a vector after the given number of
    generations.

    Args:
        freqs: a matrix of frequencies.
        n_generations: number of generations.
        size: effective size of population.
    """

    freqs = np.asarray(freqs)
    if freqs.ndim == 1:
        freqs = frequency_drift_1D(freqs, n_generations, size)
        return fill_freqs_vector(freqs)
    elif freqs.shape[1] == 2:
        freqs_vector = flatten_frequencies(freqs)
        freqs = frequency_drift_1D(freqs_vector, n_generations, size)
        return fill_freqs_vector(freqs)
    else:
        raise NotImplementedError('only biallelic data is supported')