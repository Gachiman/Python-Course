def input_string():
    while True:
        try:
            string = int(input("Enter the string: "))
            return string
        except ValueError:
            print("Please reinsert.")


def main():
    string = str(input_string())
    occurrences = []
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            occurrences.append([count, string[i - 1]])
            count = 1
    else:
        occurrences.append([count, string[i - 1]])

    for character in range(len(occurrences)):
        print("({0}, {1})".format(occurrences[character][0], occurrences[character][1]), end=" ")


if __name__ == "__main__":
    main()
