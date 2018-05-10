# This is a program to check if the Elgamal encryption
# in the PyCrypto library is a homomorphic encryption or not

# Import all the required libraries
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
import time
import sys

# Generate a 256 or 1024 bit key to use for ELgamal encryption
start = time.time()
key = ElGamal.generate(256, Random.new().read)  # Change 256 to 1024 for more secure encryption
print("Time taken to generate the key: ", time.time() - start)

# Main method
def main():
    # Run this until the user exits
    while True:
        # Take two integers as input
        x = int(input("Enter an integer or -1 to exit: "))
        if x == -1:
            break
        y = int(input("Enter another integer: "))

        # Generate r for g^r
        while 1:
            k1 = random.StrongRandom().randint(1, key.p-1)
            if GCD(k1, key.p-1) == 1:
                break

        # Encrypt the first integer
        encryption_1 = key.encrypt(x, k1)

        # Generate another r for g^r
        while 1:
            k2 = random.StrongRandom().randint(1, key.p-1)
            if GCD(k2, key.p-1) == 1:
                break

        # Encrypt the second integer
        encryption_2 = key.encrypt(y, k2)

        # Make Enc(x)*Enc(y)
        mult_enc = (encryption_1[0]*encryption_2[0], encryption_1[1]*encryption_2[1])

        # Decrypt Enc(x)*Enc(y)
        new_decryption = key.decrypt(mult_enc)

        # Compare the decryption with actual multiplication
        if new_decryption != x*y:
            print("Encryption not homomorphic")
        else:
            print(new_decryption,"==", x*y, "Encryption is homomorphic")


if __name__ == '__main__': main()