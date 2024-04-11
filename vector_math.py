import functools as ft


def add(u, v):
    return [a + b for (a, b) in zip(u, v)]


def sum(vs):
    return ft.reduce(add, vs, [0] * len(vs[0]))


def dot(u, v):
    return sum([a * b for (a, b) in zip(u, v)])


def norm(v):
    mag = dot_product(v, v) ** (1 / 2)
    return [x / mag for x in v]
