def merge_the_tools(string, k):
    if (k > len(string)) or (len(string) % k != 0):
        return
    parts = [string[i:i+k] for i in range(0, len(string), k)]
    for i in range(len(parts)):
        print("".join(dict.fromkeys(parts[i])))


if __name__ == '__main__':
    string_, k_ = input(), int(input())
    merge_the_tools(string_, k_)
