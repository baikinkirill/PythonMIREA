import math


def main(y):
    if (y < -31):
        return 5 * (abs(y ** 3)) ** 4 + y ** 5
    elif (-31 <= y < 47):
        return (1 + y + y ** 3) ** 3 + 75 + y ** 4
    elif (47 <= y < 73):
        return (y ** 6 - 7 * (0.01 - y ** 2 - 41 * y) ** 5)
    else:
        return y ** 15 + math.log(y) ** 2 + 98 * y ** 6


print("{:e}".format(main(65)))
