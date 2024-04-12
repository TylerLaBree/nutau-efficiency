import functools as ft


def add(u, v):
    if not (len(u) == len(v)):
        print("ERROR in vector_math.add(u, v): vectors not same length")
        return None
    return [a + b for (a, b) in zip(u, v)]


def vsum(vs):
    if len(vs) == 0:
        return 0
    return ft.reduce(add, vs, [0] * len(vs[0]))


def dot(u, v):
    if not (len(u) == len(v)):
        print("ERROR in vector_math.dot(u, v): vectors not same length")
        return None
    return sum([a * b for (a, b) in zip(u, v)])


def cross(u, v):
    if not (len(u) == len(v) == 3):
        print("ERROR in vector_math.cross(u, v): vectors not length 3")
        return None
    return [
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    ]


def magnitude(v):
    return dot(v, v) ** (1 / 2)


def norm(v):
    mag = magnitude(v)
    return [x / mag for x in v]
