#! /usr/bin/python3

import challenge33_iDH
#import challenge36_SRP
import hashlib
from Crypto import Random
import os
import binascii
from Crypto.Util import number

N=number.getStrongPrime(512)

g = 2
if __name__ == '__main__':
    # S
    salt = Random.new().read(16)
    #P = challenge36_SRP.P
    P="5702039"
    x = hashlib.sha256(salt + bytes(P, 'utf-8'))
    v = pow(g, int(x.hexdigest(), 16), N)
    print(v)
    # C -> S
    #I = challenge36_SRP.I
    I="a959695@live.com"
    A = pow(g, challenge33_iDH.a, N)
    # S -> C
    B = pow(g, challenge33_iDH.b, N)
    # C
    u = binascii.hexlify(os.urandom(128))
    u = int(u, 16)
    print('u', u)
    C_S = pow(B, (challenge33_iDH.a + u * int(x.hexdigest(), 16)), N)
    print('C_S', C_S)
    C_K = hashlib.sha256(str(C_S).encode()).hexdigest()
    print('C_K', C_K)
    # S
    S_S = pow(A * pow(v, u, N), challenge33_iDH.b, N)
    print('S_S', S_S)
    S_K = hashlib.sha256(str(S_S).encode()).hexdigest()
    print('S_K:', S_K)
    # C -> S Send HMAC-SHA256(K, salt)
    C2S = hashlib.pbkdf2_hmac('sha256', bytes(str(C_K), 'utf-8'), salt, 10000)
    print('C2S:', str(C2S))
    # S -> C Send "OK" if HMAC-SHA256(K, salt) validates
    S2C = hashlib.pbkdf2_hmac('sha256', bytes(str(S_K), 'utf-8'), salt, 10000)
    print('S2C:', S2C)
    if C2S == S2C:
        print('OK')

    #Ricky-Hao
    pass_list=[]
    with open("./dic.txt",'r') as f:
        for p in f.readlines():
            pass_list.append(p.strip('\n'))

    for pa in pass_list:
        x = hashlib.sha256(salt + bytes(pa, 'utf-8'))
        v = pow(g, int(x.hexdigest(), 16), N)
        A = pow(g, challenge33_iDH.a, N)
        S=pow(A * pow(v, u, N), challenge33_iDH.b, N)
        K = hashlib.sha256(str(S).encode()).hexdigest()
        temp=hashlib.pbkdf2_hmac('sha256', bytes(str(K), 'utf-8'), salt, 10000)
        if(temp==S2C):
            print(pa)
            break

