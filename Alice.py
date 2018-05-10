from Crypto import Random
from Crypto.PublicKey import ElGamal
from Crypto.Random import random
from Crypto.Util.number import GCD
from time import time
import socket
import pickle
import sys


def recvall(sock):
    data = b''
    while True:
        packet = sock.recv(4096)
        data += packet
        if len(packet) < 4096:
            break
    return data


x = int(input("Enter your integer: "))
if x < 0:
    sys.exit("You entered a negative number")
x = bin(x)[2:]
x = x[::-1]


# Generate a private key pk and secret key sk

start = time()
key = ElGamal.generate(256, Random.new().read)
print("Time taken to generate the key:", time() - start, "seconds")
while 1:
    k = random.StrongRandom().randint(1,key.p-1)
    if GCD(k,key.p-1) == 1:
        break


# Prepare a 2 x n table named T
# T[xi, i] = E(1)
# T[xi', i] = E(r)
#
T0 = []
T1 = []
# print(x)
for i in range(len(x)):
    while 1:
        k = random.StrongRandom().randint(1, key.p - 1)
        if GCD(k, key.p - 1) == 1:
            break
    r = random.StrongRandom().randint(1,key.p-1)
    # print(r)
    if x[i] == '0':
        T0.append(key.encrypt(1, k))
        T1.append(key.encrypt(r, k))
    else:
        T0.append(key.encrypt(r, k))
        T1.append(key.encrypt(1, k))

T = [T0,T1]
# Pass the T to Bob

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

print("Connected to BOB at: ", addr)
data_stream1 = pickle.dumps(T)
conn.send(data_stream1)
# print("Sent T")

confirmation_message = conn.recv(4096)
confirmation_message = confirmation_message.decode()
if confirmation_message == '0':
    print("Your number is less than Bob's")
    sys.exit()

data = b""
print("Recieving data")
data = recvall(conn)
print("received all the data")

ciphertext = pickle.loads(data)
decryptions = []
for i in ciphertext:
    decryptions.append(key.decrypt(i))

flag = 0

for i in decryptions:
    if i == 1:
        print("Your number is greater than Bob's")
        conn.send("Your number is less than or equal to Alice's".encode())
        flag = 1
        break

if flag == 0:
    print("Your number is less than or equal to Bob's")
    conn.send("Your number is greater than Alice's".encode())

conn.close()