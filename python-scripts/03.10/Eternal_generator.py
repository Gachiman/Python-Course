def eternal_gen():
    while True:
        yield "You are sorcerer, Garry."


def main():
    gen = eternal_gen()
    for i in gen:
        print(i)


if __name__ == "__main__":
    main()
