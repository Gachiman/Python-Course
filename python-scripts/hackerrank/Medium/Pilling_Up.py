def main(cubs_num, cubs):
    while len(cubs) > 1:
        if cubs[0] >= cubs[1] or cubs[0] >= cubs[-1]:
            if cubs[-1] >= cubs[1]:
                cubs.pop(-1)
            else:
                cubs.pop(1)
        else:
            return "No"
    return "Yes"


if __name__ == "__main__":
    for i in range(int(input())):
        cubs_num_ = int(input())
        cubs_ = list(map(int, input().split()))
        print(main(cubs_num_, cubs_))
