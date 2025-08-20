# utils.py
def print_line():
    """Prints a single line of 50 equals signs."""
    print(50 * "=")

def print_n_lines(n: int):
    """Prints `n` lines of 50 equals signs each."""
    for _ in range(n):
        print_line()

