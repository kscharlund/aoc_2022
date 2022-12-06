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


def get_data():
    return [line.strip() for line in open(sys.argv[1])]


def a(data):
    for line in data:
        for start in range(len(line)):
            if len(set(line[start : start + 4])) == 4:
                print(start + 4)
                break
        else:
            print("Huh?")


def b(data):
    for line in data:
        for start in range(len(line)):
            if len(set(line[start : start + 14])) == 14:
                print(start + 14)
                break
        else:
            print("Huh?")


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
