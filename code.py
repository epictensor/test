def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number.

    Args:
        n (int): Position in Fibonacci sequence (0-indexed)

    Returns:
        int: Fibonacci number at position n
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


if __name__ == "__main__":
    n = 10
    print(f"Fibonacci({n}) = {fibonacci(n)}")
