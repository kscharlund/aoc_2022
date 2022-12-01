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


def read_inventories() -> list[int]:
    inventories = []
    current_inventory = []
    for line in open(sys.argv[1]):
        if not line.strip():
            inventories.append(current_inventory)
            current_inventory = []
        else:
            current_inventory.append(int(line))
    inventories.append(current_inventory)
    return inventories


def a():
    print(max(sum(inv) for inv in read_inventories()))


def b():
    sums = sorted(sum(inv) for inv in read_inventories())
    print(sum(sums[-3:]))


def main():
    a()
    print()
    b()


if __name__ == "__main__":
    main()
