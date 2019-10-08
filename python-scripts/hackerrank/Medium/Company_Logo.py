import collections


def main(string):
    words = collections.Counter(string).most_common()
    words = sorted(words, key = lambda x: (-x[1], x[0]))
    for ch, count in words[:3]:
        print(ch, count)


if __name__ == '__main__':
    s = input()
    main(s)
