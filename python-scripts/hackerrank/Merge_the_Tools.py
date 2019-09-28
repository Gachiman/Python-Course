def merge_the_tools(string, k):
    if (k > len(string)) or (len(string) % k != 0):
        return
    parts = [string[i:i+k] for i in range(0, len(string), k)]
    for i in range(len(parts)):
        final_part = []
        for item in parts[i]:
            if item not in final_part:
                final_part.append(item)
        parts[i] = "".join(final_part)
    for item in parts:
        print(item)


if __name__ == '__main__':
    string_, k_ = input(), int(input())
    merge_the_tools(string_, k_)
