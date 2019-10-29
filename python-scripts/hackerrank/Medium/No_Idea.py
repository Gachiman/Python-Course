def main():
    n = input().split()
    m = input().split()
    like_set = set(input().split())
    dislike_set = set(input().split())
    happiness = 0

    for item in m:
        if item in like_set:
            happiness += 1
        elif item in dislike_set:
            happiness -= 1

    print(happiness)


if __name__ == "__main__":
    main()
