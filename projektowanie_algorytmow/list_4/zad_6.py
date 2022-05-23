import random
import math

p = 23
q = 7
n = p * q
phi = (p - 1) * (q - 1)

def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l

e=int(input())
d = modinv(e, phi)
print(f'public key: e= {str(e)} n= {str(n)}')
print(f'private key: d= {str(d)} n= {str(n)}')

def encrypt_block(m):
    return modinv(m**e, n)


def decrypt_block(c):
    return modinv(c**d, n)


def encrypt_string(s):
    return ''.join(str(chr(encrypt_block(ord(x)))) for x in s)


def decrypt_string(s):
    return ''.join(str(chr(decrypt_block(ord(x)))) for x in s)


s = input("Enter a message to encrypt: ")
print("\nPlain message: " + s + "\n")

enc = encrypt_string(s)
print("Encrypted message: " + enc + "\n")
dec = decrypt_string(enc)
print("Decrypted message: " + dec + "\n")