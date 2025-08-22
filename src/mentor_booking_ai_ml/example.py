"""Example module containing simple add function."""

from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Return the sum of ``a`` and ``b``.

    Args:
        a: First addend.
        b: Second addend.

    Returns:
        The sum of ``a`` and ``b``.
    """
    return a + b
