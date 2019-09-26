vowels = ('A', 'E', 'I', 'O', 'U')


def minion_game(string):
    index = 0
    stuart_score = 0
    kevin_score = 0

    for ch in string:
        if ch in vowels:
            kevin_score += len(string) - index
        else:
            stuart_score += len(string) - index
        index += 1

    if stuart_score > kevin_score:
        print("Stuart {}".format(stuart_score))
    elif stuart_score < kevin_score:
        print("Kevin {}".format(kevin_score))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input().upper()
    for item in s:
        if item.isdigit():
            break
    else:
        minion_game(s)
