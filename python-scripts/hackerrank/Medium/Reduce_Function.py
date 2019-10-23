from fractions import Fraction
from functools import reduce


def product(rat_nums):
    res = reduce(lambda x, y: x * y, rat_nums)
    return res.numerator, res.denominator


if __name__ == '__main__':
    fractions = []
    for _ in range(int(input())):
        fractions.append(Fraction(*map(int, input().split())))
    result = product(fractions)
    print(*result)
