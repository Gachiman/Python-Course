import collections


def main():
    n = int(input())
    words = collections.defaultdict(int)
    for _ in range(n):
        word = input()
        words[word] += 1
    print(len(words))
    print(" ".join(map(str, words.values())))


if __name__ == "__main__":
    main()
