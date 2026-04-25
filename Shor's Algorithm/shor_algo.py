"""
Shor's Algorithm Implementation

This script implements a classical demonstration of Shor's factoring algorithm.
It uses classical order finding (via sympy) instead of quantum order finding for simplicity.

Author: Jinal Soni
Date: March 15, 2026
"""

import random
from sympy.ntheory import n_order


def gcd(x, y):
    """
    Compute the greatest common divisor of x and y.

    Args:
        x (int): First number.
        y (int): Second number.

    Returns:
        int: GCD of x and y.
    """
    while y:
        x, y = y, x % y
    return x


def find_factors(N, a, r):
    """
    Find potential factors using the order r.

    Args:
        N (int): Number to factor.
        a (int): Base number.
        r (int): Order of a modulo N.

    Returns:
        tuple: Potential factors (factor1, factor2).
    """
    factor1 = gcd(pow(a, r // 2) - 1, N)
    factor2 = gcd(pow(a, r // 2) + 1, N)
    return factor1, factor2


def shor_algorithm(N):
    """
    Run Shor's algorithm to factor N.

    Args:
        N (int): Number to factor.

    Returns:
        None: Prints the results.
    """
    print(f"Attempting to factor N = {N}")

    # Choose random a
    a = random.randint(2, N - 1)
    print(f"Randomly chosen a: {a}")

    # Compute gcd(a, N)
    p = gcd(a, N)
    print(f"GCD of {a} and {N} is: {p}")

    if p > 1:
        print(f"Non-trivial factor found: {p}")
        print(f"Other factor q: {N // p}")
        print("We have successfully factored N. No quantum order finding needed!")
        return

    print("a and N are coprime, proceeding with order finding...")

    # Find order r (classically for demonstration)
    r = n_order(a, N)
    print(f"Order r of a mod N is: {r}")

    if r % 2 != 0:
        print("Order r is not even, need to choose a new a and repeat the process.")
        return

    # Calculate potential factors
    factor1, factor2 = find_factors(N, a, r)
    print(f"Potential factors from order r: {factor1} and {factor2}")

    if factor1 > 1 and factor1 < N:
        print(f"Non-trivial factor found: {factor1}")
    else:
        print("Factor from r/2 - 1 is trivial.")

    if factor2 > 1 and factor2 < N:
        print(f"Non-trivial factor found: {factor2}")
    else:
        print("Factor from r/2 + 1 is trivial.")


def main():
    """
    Main function to run Shor's algorithm demonstration.
    """
    N = 15
    shor_algorithm(N)


if __name__ == "__main__":
    main()