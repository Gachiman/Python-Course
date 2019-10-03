from math import ceil


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def x_range(stop, start=None, step=None):
    if isinstance(start, type(None)):
        start = 0
        step = 1
    elif isinstance(start, int):
        start, stop = stop, start
        if isinstance(step, type(None)):
            step = 1
        elif not isinstance(step, int):
            raise TypeError
        elif step == 0:
            raise ValueError
        elif sign(step) < 0:
            start, stop = stop, start
            step = abs(step)
    else:
        raise TypeError

    x_list = [None] * ceil((stop - start) / step)
    i = 0
    while start < stop:
        x_list[i] = start
        start += step
        i += 1
    return x_list


def main():
    print(x_range(5, -5, -2))


if __name__ == "__main__":
    main()
