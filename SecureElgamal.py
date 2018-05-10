from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
import time

start = time.time()

key = ElGamal.generate(1024, Random.new().read)
key2 = ElGamal.generate(1024, Random.new().read)

print("Time taken to generate the keys: ", time.time() - start)

while 1:
    k = random.StrongRandom().randint(1, key.p-1)
    if GCD(k, key.p-1) == 1:
        break

x = key.encrypt(1, k)
