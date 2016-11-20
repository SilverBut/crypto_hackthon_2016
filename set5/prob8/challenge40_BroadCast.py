#! /usr/bin/python3

import challenge39_RSA
from Crypto.Util.number import getPrime
import binascii


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m

"""Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
"""
def find_invpow(x,n):
    high = 1
    while high ** n < x:
        high *= 2
    low = high/2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

e = 3
public_key = [getPrime(1024) * getPrime(1024) for i in range(3)]
print("Please input a message (Recommand input message length < 40):")
message = input()
cipher = [pow(int(binascii.hexlify(message.encode()), 16), e, n) for n in public_key]
print("Three cipher with different public key:")
for c in cipher:
    print(c)
    print(' ')
c0, c1, c2 = [c % n for c,n in zip(cipher, public_key)]
n0, n1, n2 = public_key
ms0 = n1 * n2
ms1 = n0 * n2
ms2 = n0 * n1
N012 = n0 * n1 * n2
result = ((c0 * ms0 * modinv(ms0, n0)) +
        (c1 * ms1 * modinv(ms1, n1)) +
        (c2 * ms2 * modinv(ms2, n2))) % N012

mseeage = find_invpow(result, e)
print("Result: ")
print(message)
