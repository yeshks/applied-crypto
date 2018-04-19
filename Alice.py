from Crypto import Random
from Crypto.PublicKey import ElGamal
from Crypto.Random import random
from Crypto.Util.number import GCD
from time import time

x = int(input())
x = bin(x)[2:]
x = x[::-1]


## Generate a private key pk and secret key sk

now = time()

key = ElGamal.generate(256, Random.new().read)
print(key.p)

print("Time taken to generate the key:", time() - now, "seconds")

while 1:
    k = random.StrongRandom().randint(1,key.p-1)
    if GCD(k,key.p-1) == 1:
        break


## Prepare a 2 x n table named T
## T[xi, i] = E(1)
## T[xi', i] = E(r)
##
T = []
print(x)
for i in range(len(x)):
    r = random.StrongRandom().randint(1,key.p-1)
    if x[i] == '1':
        T.append([key.encrypt(1, k), key.encrypt(r, k)])
    else:
        T.append([key.encrypt(r, k), key.encrypt(1, k)])

print(T)
