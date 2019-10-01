import datetime
import calendar


def time_delta(t1, t2):
    t1 = t1.split()
    t2 = t2.split()

    utf_1 = int(t1[5][1:3]) * 60 + int(t1[5][3:])
    utf_2 = int(t2[5][1:3]) * 60 + int(t2[5][3:])
    hrs = int(t1[4][0:2]) - int(t2[4][0:2])
    mns = int(t1[4][3:5]) - int(t2[4][3:5])
    secs = int(t1[4][6:]) - int(t2[4][6:])
    month1 = t1[2]
    month2 = t2[2]
    d0 = datetime.date(int(t1[3]), list(calendar.month_abbr).index(month1), int(t1[1]))
    d1 = datetime.date(int(t2[3]), list(calendar.month_abbr).index(month2), int(t2[1]))
    delta = d0 - d1
    days = delta.days

    if t1[5][0] == "-":
        mns += utf_1
    else:
        mns -= utf_1

    if t2[5][0] == "-":
        mns -= utf_2
    else:
        mns += utf_2

    difference = days * 86400 + hrs * 3600 + mns * 60 + secs
    return abs(difference)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1_ = input()
        t2_ = input()

        delta_ = time_delta(t1_, t2_)
        print(delta_)
