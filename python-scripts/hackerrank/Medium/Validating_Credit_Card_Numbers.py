import re


def check(string):
    if re.search(r"[4-6]\d{3}(?:-\d{4}){3}", string):
        string = re.sub(r"-", "", string)
    if re.search(r"\b[4-6](?:(\d)(?!\1\1\1)){15}\b", string):
        return 'Valid'
    else:
        return 'Invalid'


if __name__ == "__main__":
    for _ in range(int(input())):
        print(check(input()))
