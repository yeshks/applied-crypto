# This is the python server that Alice can run on her computer
# Alice enters the private number she has and gets the final result as the output

# Import all the required libraries
from Crypto import Random
from Crypto.PublicKey import ElGamal
from Crypto.Random import random
from Crypto.Util.number import GCD
from time import time
import socket
import pickle
import sys

# Method to recieve all the packets of a information if the information is greater than 4 kb
def recvall(sock):
    data = b''
    while True:
        packet = sock.recv(4096)
        data += packet
        if len(packet) < 4096:
            break
    return data


# Take the private input from Alice
x = int(input("Enter your integer: "))
# If the number is negative exit the system
if x < 0:
    sys.exit("You entered a negative number")
# Calculate the binary and then reverse the binary string
# for ease of indexing
x = bin(x)[2:]
x = x[::-1]


# Generate the Elgamal key and print the time requires to do so

start = time()
key = ElGamal.generate(256, Random.new().read)
print("Time taken to generate the key:", time() - start, "seconds")


# Prepare a 2 x n table named T
# T[xi, i] = E(1)
# T[xi', i] = E(r)
T0 = []
T1 = []
for i in range(len(x)):
    while 1:
        k = random.StrongRandom().randint(1, key.p - 1)
        if GCD(k, key.p - 1) == 1:
            break
    r = random.StrongRandom().randint(1,key.p-1)
    if x[i] == '0':
        T0.append(key.encrypt(1, k))
        T1.append(key.encrypt(r, k))
    else:
        T0.append(key.encrypt(r, k))
        T1.append(key.encrypt(1, k))
T = [T0,T1]

# Pass the T array to Bob over a socket

# Connect to Bob
HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

print("Connected to BOB at: ", addr)

T = pickle.dumps(T)
conn.sendall(T)

# Alice receives a confirmation message
confirmation_message = conn.recv(4096)
confirmation_message = confirmation_message.decode()

if confirmation_message == '0':
    print("Your number is less than Bob's")
    sys.exit()

ct = b""
print("Recieving data")
ct = recvall(conn)
print("received all the data")

ciphertext = pickle.loads(ct)
decryptions = []
for i in ciphertext:
    decryptions.append(key.decrypt(i))

# Initialize a flag so that you know if 1 was encountered or not
flag = 0

# Send the appropriate message according to the logic proposed in the paper
for i in decryptions:
    if i == 1:
        print("Your number is greater than Bob's")
        conn.send("Your number is less than or equal to Alice's".encode())
        flag = 1
        break

if flag == 0:
    print("Your number is less than or equal to Bob's")
    conn.send("Your number is greater than Alice's".encode())

# Close the socket connection
conn.close()