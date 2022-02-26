import math


def main(x):
    n = len(x)
    result = 0

    for i in range(1, n + 1):
        result += 23 * (13 * x[n - i] -
                        54 * (x[math.ceil(i / 3 - 1)]
                              ** 2) - 65) ** 3

    return 38 * result


print("{:e}".format(main([-0.12, 0.36, -0.81, -1.0, -0.23, 0.62, 0.62, 0.58])))
