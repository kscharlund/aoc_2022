import sys
from pprint import pprint
import math


def memoize(func):
    """
    Memoization decorator for a function taking a single argument.
    """
    class Memodict(dict):
        """Memoization dictionary."""
        def __missing__(self, key):
            ret = self[key] = func(key)
            return ret
    return Memodict().__getitem__


def a():
    pass


def b():
    pass


def main():
    a()
    print()
    b()


if __name__ == '__main__':
    main()
