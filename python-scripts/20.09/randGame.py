import random


def main():
    number = random.randint(1, 9)
    answer = input("Let's start, enter you number from 1 to 9: ")
    while answer.lower() != 'exit':
        answer = int(answer)
        if answer == number:
            print("Congratulations, you are great!")
            break
        elif answer < number:
            print("Too low.")
        else:
            print("too high")
        answer = input("Try again: ")


if __name__ == "__main__":
    main()
