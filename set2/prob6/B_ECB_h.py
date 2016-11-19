__author__ = 'Administrator'
import R_ECB_CBC, pkcs7
import random
import AES_ECB
import math

r_pre=R_ECB_CBC.random_key(random.randint(0,255))
key = R_ECB_CBC.random_key(16)
def encrypt_withs(ys,us):
    m=pkcs7.pkcs7(r_pre+ys+us, 16)
    return AES_ECB.encrypt(m,key)

def getblocksize(us):
    ys='aa'
    i=2
    l=0
    while True:
        c=encrypt_withs(ys,us)
        if l==0:
            l=len(c)
            ys+='aa'
            continue
        elif l==len(c):
            ys+='aa'
            continue
        else:
            return len(c)-l

def getpresize(us):
    ys=''
    i=0
    l=0
    while True:
        c=encrypt_withs(ys,us)
        if l==0:
            l=len(c)
            ys+='aa'
            i+=2
            continue
        elif l==len(c):
            ys+='aa'
            i+=2
            continue
        else:
            return l-len(us)-i


def b_ECB(us):
    size = getblocksize(us)
    presize=getpresize(us)
    fsize=int(math.ceil(presize*1.0/size))*size
    pre='a'*(fsize-presize)
    m = ''
    for i in range(1, len(us)+1):
        pad = (size-i % size)*'a'
        if len(m) >= size-1:
            ys = m[-15:]
        else:
            ys = 'a'*(size-1-len(m))+m
        for j in range(0, 256):
            c = encrypt_withs(pre+ys+chr(j)+pad, us)
            if c[fsize:fsize+size] == c[fsize+len(ys)+len(pad)+1+i-size:fsize+len(ys)+len(pad)+1+i]:
                m += chr(j)
                break
    return m

if __name__ == '__main__':
    bm = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'
    m = HexBase64.base642hex(bm).decode('hex')
    print m
    print b_ECB(m)