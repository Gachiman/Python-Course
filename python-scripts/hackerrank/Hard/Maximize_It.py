import itertools


def main(lists_count, divider, lists):
    maximum = 0
    test = 0
    for item in itertools.product(*lists):
        test = sum(map(lambda x: x**2, item)) % divider
        if test > maximum:
            maximum = test
    print(maximum)


if __name__ == "__main__":
    lists_count_, divider_ = map(int, input().split())
    lists_ = []
    for _ in range(lists_count_):
        lists_.append(list(map(int, input().split()))[1:])
    main(lists_count_, divider_, lists_)
