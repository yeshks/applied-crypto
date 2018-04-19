# Converting the comparison problem to a set intersection problem
# This is a program to validate the logic mentioned in the paper


# Method to get the zero encoding of the integer specified with a padding
# params int x, int padding
def make_zero_encoding(x, padding=256):
    x = bin(x)[2:].zfill(padding)  # Pad the binary integer
    x = x[::-1]  # Reverse the binary integer so the order stays as per the formula specified in the paper
    zero_encoding = set()  # Initialize an empty set
    for i in range(len(x)):
        if x[i] == '0':
            if x[i + 1:] == '0' * len(x[i + 1:]):
                break
            element = "1" + x[i + 1:]
            element = element[::-1]
            zero_encoding.add(int(element, 2))
    return zero_encoding  # Return the set


# Method to get the one encoding of the integer specified with a padding
# params int x, int padding
def make_one_encoding(x, padding=256):
    x = bin(x)[2:].zfill(padding)  # Pad the binary integer
    x = x[::-1]  # Reverse the binary integer so the order stays as per the formula specified in the paper
    one_encoding = set()  # Initialize an empty set
    for i in range(len(x)):
        if x[i] == '1':
            if x[i + 1:] == '0' * len(x[i + 1:]):
                break
            element = x[i:]
            element = element[::-1]
            one_encoding.add(int(element, 2))
    return one_encoding  # Return the set

# Main method of how the program will run
def main():
    x = int(input("Enter x = "))
    y = int(input("Enter y = "))

    print("Zero encoding of x: ", make_zero_encoding(x))
    print("One encoding of y: ", make_one_encoding(y))

    set_intersect = set.intersection(make_zero_encoding(x), make_one_encoding(y))

    if len(set_intersect) == 0:
        print('x is greater than y')
    else:
        print('x is less than y')


if __name__ == '__main__': main()
