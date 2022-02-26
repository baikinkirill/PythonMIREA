import math


def main(n):
    if (n == 0):
        return -0.280
    elif (n >= 1):
        return (math.atan(main(n - 1)
                          ** 2 + 1.0 + 4
                          * main(n - 1) ** 3)) ** 3
    else:
        return 0


print("{:e}".format(main(8)))
