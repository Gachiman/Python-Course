def main():
    n = int(input())
    words = {}
    for i in range(n):
        word = input()
        words[word] = words.get(word, 0) + 1
    print(len(words))
    print(" ".join(map(str, words.values())))


if __name__ == "__main__":
    main()
