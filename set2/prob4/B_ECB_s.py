__author__ = 'Administrator'
import R_ECB_CBC, pkcs7
import AES_ECB,HexBase64

key = R_ECB_CBC.random_key(16)
def encrypt_withs(ys,us):
    m=pkcs7.pkcs7(ys+us, 16)
    return AES_ECB.encrypt(m,key)

def getblocksize(us):
    ys='aa'
    i=2
    while True:
        c=encrypt_withs(ys,us)
        if c[0:i/2]==c[i/2:i]:
            return i/2
        i+=2
        ys+='aa'
        if i == 34:
            return

def gettype(us):
    size=getblocksize(us)
    if len(encrypt_withs('',us))==len(us)/size*size+size:
        return 'ECB'
    else:
        return 'CBC'

def b_ECB(us):
    size = getblocksize(us)
    m = ''
    if gettype(us) == 'CBC':
        return 'error'
    for i in range(1, len(us)+1):
        pad = (size-i % size)*'a'
        if len(m) >= size-1:
            ys = m[-15:]
        else:
            ys = 'a'*(size-1-len(m))+m
        for j in range(0, 256):
            c = encrypt_withs(ys+chr(j)+pad, us)
            if c[0:size] == c[len(ys)+len(pad)+1+i-size:len(ys)+len(pad)+1+i]:
                m += chr(j)
                break
    return m

if __name__ == '__main__':
    bm = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'
    m = HexBase64.base642hex(bm).decode('hex')
    print b_ECB(m)
    print m