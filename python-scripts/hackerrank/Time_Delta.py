import datetime


def time_delta(t1, t2):
    t1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return abs(int((t1-t2).total_seconds()))


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1_ = input()
        t2_ = input()

        delta_ = time_delta(t1_, t2_)
        print(delta_)
