import math


def main(b, a):
    result = 0

    for j in range(1, b + 1):
        left = ((math.atan(j ** 3 - j ** 2)) ** 4) / (51.0)
        right = 21.0 * (math.atan(j) ** 7)
        result += left + right

    for i in range(1, a + 1):
        result += 1 + i ** 6 + i ** 3

    return result


print("{:e}".format(main(8, 4)))
