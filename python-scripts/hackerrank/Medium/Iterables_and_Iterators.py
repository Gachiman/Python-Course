import itertools


def main(n, letters, k):
    comb = itertools.combinations(letters, k)
    all_comb, need = 0, 0
    for ch in comb:
        all_comb += 1
        if 'a' in ch:
            need += 1
    print(need / all_comb)


if __name__ == '__main__':
    main(int(input()), input().split(), int(input()))
