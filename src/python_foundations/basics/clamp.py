def clamp(x: float, lo: float, hi: float) -> float:
    """
    Clamp x to the interval [lo, hi].

    Args:
        x: Value to clamp.
        lo: Lower bound.
        hi: Upper bound.

    Returns:
        Clamped value.

    Raises:
        ValueError: If lo > hi.
    """
    if lo > hi:
        raise ValueError("lo must be <= hi")

    if x < lo:
        return lo
    if x > hi:
        return hi
    return x
