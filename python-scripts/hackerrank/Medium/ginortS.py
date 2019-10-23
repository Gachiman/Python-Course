def sortlol(ch):
    if 'a' <= ch <= 'z':
        return 0
    elif 'A' <= ch <= 'Z':
        return 1
    elif int(ch) % 2 == 1:
        return 2
    else:
        return 3


def main(string):
    print("".join(sorted(string, key=lambda x: (sortlol(x), x))))


if __name__ == "__main__":
    main(input())