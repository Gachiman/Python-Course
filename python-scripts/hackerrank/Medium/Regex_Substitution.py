import re


def main(string):
    lol = {'&&': 'and', '||': 'or'}
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: lol[x.group()], string))


if __name__ == "__main__":
    s = ''
    for _ in range(int(input())):
        s += input() + '\n'
    main(s)
