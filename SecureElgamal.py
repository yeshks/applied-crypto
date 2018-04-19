from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
from Crypto.Hash import SHA
import time

now = time.time()
message = "Hello".encode()
key = ElGamal.generate(256, Random.new().read)
print("Time taken: ", time.time() - now)
# h = SHA.new(message).digest()
while 1:
    k = random.StrongRandom().randint(1,key.p-1)
    if GCD(k,key.p-1)==1: break

x = key.encrypt(1, k)
y = key.encrypt(9, k)
z = key.encrypt(1, k)

z = (x[0]*y[0]*z[0], x[1]*y[1]*z[1])
print(key.decrypt(z))
# sig = key.sign(h,k)
# ...
# if key.verify(h,sig):
#     print("OK")
# else:
#     print("Incorrect signature")