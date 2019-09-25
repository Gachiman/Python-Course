import math


def input_length_side(val):
    while True:
        try:
            length = int(float(input("Enter the length of side {0} (0 < {0} <= 100): ".format(val))))
            if 0 < length <= 100:
                return length
            else:
                raise ValueError
        except ValueError:
            print("Please reinsert")


def main():
    side_ab = input_length_side("AB")
    side_bc = input_length_side("BC")
    tg_mbc = side_ab / side_bc
    angle_mbc = math.degrees(math.atan(tg_mbc))
    print(round(angle_mbc), '°', sep='')


if __name__ == '__main__':
    main()
