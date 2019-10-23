def main(n, m, arr, k):
    for item in sorted(arr, key=lambda x: x[k]):
        print(*item)


if __name__ == '__main__':
    _n, _m = map(int, input().split())
    _arr = []
    for _ in range(_n):
        _arr.append(list(map(int, input().rstrip().split())))
    _k = int(input())
    main(_n, _m, _arr, _k)
