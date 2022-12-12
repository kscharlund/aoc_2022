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


def height(cc):
    if cc == "S":
        return ord("a")
    if cc == "E":
        return ord("z")
    return ord(cc)


def get_data():
    grid = open(sys.argv[1]).read().splitlines()
    rows, cols = len(grid), len(grid[0])
    adj = [[] for _ in range(rows * cols)]
    src = dst = -1
    srcs = []
    for row in range(rows):
        for col in range(cols):
            idx = row * cols + col
            cc = grid[row][col]
            if cc == "S":
                src = idx
                cc = "a"
            elif cc == "E":
                dst = idx
                cc = "z"
            if cc == "a":
                srcs.append(idx)
            hh = ord(cc)
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = row + dy, col + dx
                if 0 <= ny < rows and 0 <= nx < cols:
                    if hh + 1 >= height(grid[ny][nx]):
                        adj[idx].append((ny * cols + nx, 1))
    return adj, src, dst, srcs


class BucketQueue:
    def __init__(self, max_dist: int):
        self._buckets = [set() for _ in range(max_dist + 1)]
        self._count = 0
        self._min_p = 0

    def extract_min(self) -> int:
        assert self._count
        self._count -= 1
        for p in range(self._min_p, len(self._buckets)):
            if self._buckets[p]:
                self._min_p = p
                return self._buckets[p].pop()

    def add_at(self, u: int, p: int) -> None:
        self._count += 1
        self._buckets[p].add(u)
        if p < self._min_p:
            self._min_p = p

    def move(self, u: int, p_old: int, p_new: int) -> None:
        self._buckets[p_old].remove(u)
        self._buckets[p_new].add(u)
        if p_new < self._min_p:
            self._min_p = p_new

    def empty(self) -> bool:
        return self._count == 0


def dijkstra_with_bucket_queue(edges, size, src):
    # Dijkstra with bucket queue
    max_dist = size
    bq = BucketQueue(max_dist)
    dist = [max_dist for _ in range(size)]
    prev = [-1 for _ in range(size)]
    bq.add_at(src, 0)
    dist[src] = 0
    for n in range(size):
        if n != src:
            bq.add_at(n, max_dist)

    while not bq.empty():
        u = bq.extract_min()
        for v, w in edges[u]:
            d = dist[u] + w
            if d < dist[v]:
                bq.move(v, dist[v], d)
                dist[v] = d
                prev[v] = u

    return dist, prev


def a(data):
    adj, src, dst, _ = data
    dist, _ = dijkstra_with_bucket_queue(adj, len(adj), src)
    print(dist[dst])


def b(data):
    adj, _, dst, srcs = data
    dists = []
    for src in srcs:
        dist, _ = dijkstra_with_bucket_queue(adj, len(adj), src)
        dists.append(dist[dst])
    print(min(dists))


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
