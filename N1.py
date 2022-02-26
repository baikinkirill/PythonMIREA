import math


def main(x, z, y):
    left = (y ** 2.0 - z ** 3.0 - 30.0 *
            ((math.log2(45.0 + x ** 3.0)) ** 6.0))
    right = (42.0 * (38.0 * x * x + (y / 41.0) +
                     42.0 * y * y * y) - ((z ** 4.0) / 49.0))
    result = left / right

    first = ((59 * z ** 2 + 91 * y) ** 6)
    second = (14 * ((99 * x) ** 5))

    return (first - second - result)



print("{:e}".format(main(-0.22, 0.66, 0.7)))
