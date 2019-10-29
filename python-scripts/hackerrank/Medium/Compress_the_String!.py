import itertools


def input_string():
    while True:
        try:
            string = int(input("Enter the string: "))
            return string
        except ValueError:
            print("Please reinsert.")


def main():
    string = str(input_string())
    for char, count in itertools.groupby(string):
        print("({0}, {1})".format(len(list(count)), char), end=" ")


if __name__ == "__main__":
    main()
