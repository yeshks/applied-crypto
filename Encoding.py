# This is a supporting library
# Defining the encoding according to their definitions
# Converting the comparison problem to a set intersection problem
# This is a program to validate the logic mentioned in the paper


# Method to get the zero encoding of the integer specified with a padding
# params int x, int padding

def make_zero_encoding(x, padding=0):
    x = bin(x)[2:].zfill(padding) # Pad the binary integer
    x = x[::-1] # Reverse the binary integer so the order stays as per the formula specified in the paper
    encoding = set() # Initialize an empty set
    for i in range(len(x)):
        if x[i] == '0':
            element = '1' + x[i+1:]
            element = element[::-1]
            if int(element, 2) == 1:
                encoding.add('1')
            else:
                encoding.add(element)
            if x[i+1:] == '0'*len(x[i+1:]):
                break
    return encoding # Return the set

# Method to get the one encoding of the integer specified with a padding
# params int x, int padding
def make_one_encoding(x, padding=0):
    x = bin(x)[2:].zfill(padding) # Pad the binary integer
    x = x[::-1] # Reverse the binary integer so the order stays as per the formula specified in the paper
    encoding = set() # Initialize an empty set
    for i in range(len(x)):
        if x[i] == '1':
            element = x[i:]
            element = element[::-1]
            if int(element,2) == 1:
                encoding.add('1')
            else:
                encoding.add(element)
            if x[i+1:] == '0'*len(x[i+1:]):
                break
    return encoding # Return the set