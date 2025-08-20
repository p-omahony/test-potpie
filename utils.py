"""
Utility functions for printing lines of "=" characters.
"""

def print_line():
    """
    Print a single line of 50 "=" characters.
    """
    print("=" * 50)

def print_n_lines(n: int):
    """
    Print `n` lines of 50 "=" characters each.

    Args:
        n (int): Number of lines to print.
    """
    for _ in range(n):
        print_line()

