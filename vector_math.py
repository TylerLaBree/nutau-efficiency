def add_vectors(xs, ys):
    return [x + y for (x, y) in zip(xs, ys)]


def dot_product(xs, ys):
    return sum([x * y for (x, y) in zip(xs, ys)])


def normalize(xs):
    mag = dot_product(xs, xs) ** (1 / 2)
    return [x / mag for x in xs]

