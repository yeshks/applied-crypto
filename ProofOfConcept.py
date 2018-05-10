# Converting the comparison problem to a set intersection problem
# This is a program to validate the logic mentioned in the paper

import Encoding
import time


# Main method
def main():
    # Input two integers
    x = int(input("Enter x = "))
    y = int(input("Enter y = "))

    # Calculate the bit lengths of the numbers
    length1 = len(bin(x)) - 2
    length2 = len(bin(y)) - 2

    # Check who has a longer bit length
    if length2 > length1:
        length = length2
    else:
        length = length1

    # Calculate the 0 and 1 encodings and then find the set intersection
    # Also check the time it takes to do this
    start = time.time()
    set_intersect = set.intersection(Encoding.make_one_encoding(x, length), Encoding.make_zero_encoding(y, length))
    print("Time taken to compare encodings: ", time.time() - start)

    # Assert the inequalities and if the inequalities fail then
    # Show the encodings of the numbers for which it failed

    if len(set_intersect) == 0:
        if x <= y:
            print(x, "is less than or equal to", y)
        else:
            print(Encoding.make_one_encoding(x, length))
            print(Encoding.make_zero_encoding(y, length))
    else:
        if x > y:
            print(x, "is greater than", y)
        else:
            print(Encoding.make_one_encoding(x, length))
            print(Encoding.make_zero_encoding(y, length))


if __name__ == '__main__':
    main()
