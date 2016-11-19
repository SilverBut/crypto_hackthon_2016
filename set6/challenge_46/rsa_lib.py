#!/usr/bin/python3


########WARNING!!!!!!!
# This file is modified based on a copy of RSA code at this address:
# https://jhafranco.com/2012/01/29/rsa-implementation-in-python/
# Be sure you noticed all modifications!!!!!!!!!!!!!
##########################################3


#
# Author: Joao H de A Franco (jhafranco@acm.org)
#
# Description: RSA implementation in Python 3
#
# Date: 2012-01-30
#
# License: Attribution-NonCommercial-ShareAlike 3.0 Unported
#          (CC BY-NC-SA 3.0)
#===========================================================
from random import randrange, getrandbits
from itertools import repeat
from functools import reduce

def getPrime(n):
    """Get a n-bit pseudo-random prime"""
    def isProbablePrime(n, t = 7):
        """Miller-Rabin primality test"""
        def isComposite(a):
            """Check if n is composite"""
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2 ** i * d, n) == n - 1:
                    return False
            return True
    
        assert n > 0
        if n < 3:
            return [False, False, True][n]
        elif not n & 1:
            return False
        else:
            s, d = 0, n - 1
            while not d & 1:
                s += 1
                d >>= 1
        for _ in repeat(None, t):
            if isComposite(randrange(2, n)):
                return False
        return True    
    
    p = getrandbits(n)
    while not isProbablePrime(p):
        p = getrandbits(n)
    return p

def inv(p, q):
    """Multiplicative inverse"""
    def xgcd(x, y):
        """Extended Euclidean Algorithm"""
        s1, s0 = 0, 1
        t1, t0 = 1, 0
        while y:
            q = x // y
            x, y = y, x % y
            s1, s0 = s0 - q * s1, s1
            t1, t0 = t0 - q * t1, t1
        return x, s0, t0      

    s, t = xgcd(p, q)[0:2]
    assert s == 1
    if t < 0:
        t += q
    return t

def genRSA(p, q):
    """Generate public and private keys"""
    phi, mod = (p - 1) * (q - 1), p * q
    if mod < 65537:
        return (3, inv(3, phi), mod)
    else:
        return (65537, inv(65537, phi), mod)    

def text2Int(text):
    """Convert a text string into an integer"""
    return reduce(lambda x, y : (x << 8) + y, map(ord, text))

def int2Int(text):
    """Convert a text string into an integer"""
    return reduce(lambda x, y : (x << 8) + y, map(int, text))

def int2Text(number, size):
    """Convert an integer into a text string"""
    text = "".join([chr((number >> j) & 0xff)
                    for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")

def int2List(number, size):
    """Convert an integer into a list of small integers"""
    return [(number >> j) & 0xff
            for j in reversed(range(0, size << 3, 8))]

def list2Int(listInt):
    """Convert a list of small integers into an integer"""
    return reduce(lambda x, y : (x << 8) + y, listInt)

def modSize(mod):
    """Return length (in bytes) of modulus"""
    modSize = len("{:02x}".format(mod)) // 2
    return modSize

def encrypt(ptext, pk, mod):
    """Encrypt message with public key"""
    size = modSize(mod)
    output = []
    while ptext:
        nbytes = min(len(ptext), size - 1)
       # aux1 = text2Int(ptext[:nbytes])
        aux1 = int2Int(ptext[:nbytes])
        assert aux1 < mod
        aux2 = pow(aux1, pk, mod)
        output += int2List(aux2, size + 2)
        ptext = ptext[size:]
    return output

def decrypt(ctext, sk, p, q):
    """Decrypt message with private key
    using the Chinese Remainder Theorem"""
    mod = p * q
    size = modSize(mod)
    output = ""
    while ctext:
        aux3 = list2Int(ctext[:size + 2])
        assert aux3 < mod
        m1 = pow(aux3, sk % (p - 1), p)
        m2 = pow(aux3, sk % (q - 1), q)
        h = (inv(q, p) * (m1 - m2)) % p
        aux4 = m2 + h * q
        output += int2Text(aux4, size)
        ctext = ctext[size + 2:]
    return output

if __name__ == "__main__":

    from math import log10
    from time import time

    def printHexList(intList):
        """Print ciphertext in hex"""
        for index, elem in enumerate(intList):
            if index % 32 == 0:
                print()            
            print("{:02x}".format(elem), end = "")
        print()

    def printLargeInteger(number):
        """Print long primes in a formatted way"""
        string = "{:02x}".format(number)
        for j in range(len(string)):
            if j % 64 == 0:
                print()
            print(string[j], end = "")
        print()

    def testCase(p, q, msg, nTimes = 1):
        """Execute test case: generate keys, encrypt message and
           decrypt resulting ciphertext"""
        print("Key size: {:0d} bits".format(round(log10(p * q) / log10(2))))
        print("Prime #1:", end = "")
        printLargeInteger(p)
        print("Prime #2:", end = "")
        printLargeInteger(q)
        print("Plaintext:", msg)
        pk, sk, mod = genRSA(p, q)
        ctext = encrypt(msg, pk, mod)
        print("Ciphertext:", end = "")
        printHexList(ctext)
        ptext = decrypt(ctext, sk, p, q)
        print("Recovered plaintext:", ptext, "\n")

    for n in [1024]:    
        t1 = time()
        p5 = getPrime(n)
        t2 = time()
        print("Elapsed time for {:0d}-bit prime ".format(n), end = "")
        print("generation: {:0.3f} s".format(round(t2 - t1, 3)))
        t3 = time()
        p6 = getPrime(n)
        t4 = time()
        print("Elapsed time for {:0d}-bit prime ".format(n), end = "")
        print("generation: {:0.3f} s".format(round(t4 - t3, 3)))
        testCase(p5, p6, "It's all greek to me")
