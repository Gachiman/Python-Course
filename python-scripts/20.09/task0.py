# Determines whether the year is a leap
def is_leap(year=2019):
    leap = False
    if year % 4 == 0:
        leap = True
        if (year % 100 == 0) and (year % 400 != 0):
            leap = False
    if leap:
        print(year, " is a leap year.")
    else:
        print(year, "is not a leap year.")


# Generates a Fibonacci sequence of a given length
def fibonacci(count=5):
    if count < 0:
        raise Exception("Must not be negative.")
    sequence = [1, 1]
    if count < 2:
        print(sequence[:count])
        return
    for i in range(count - 2):
        sequence.append(sequence[-2] + sequence[-1])
    print(sequence)


# Displays the largest number in the list
def list_max(array=None):
    if array is None:
        array = [3, 7, 0, -2, 11, 7]
    max_elem = array[0]
    for elem in array:
        if elem > max_elem:
            max_elem = elem
    print(max_elem)


def main():
    is_leap(2400)
    fibonacci(10)
    list_max()


if __name__ == "__main__":
    main()
