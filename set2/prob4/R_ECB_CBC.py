__author__ = 'Administrator'
import random
import AES_CBC_H,pkcs7
import set1.AES_ECB

def random_key(l):
    if l%2!=0:
        l-=1
    return ''.join([chr(random.randint(0,255)) for i in range(0,l)])

def random_padm(m):
    return random_key(random.randint(5,10))+m+random_key(random.randint(5,10))

def random_encrypto(m):
    key = random_key(16)
    m = pkcs7.pkcs7(random_padm(m), 16)
    #ECB
    if random.randint(1, 2) == 1:
        return set1.AES_ECB.encrypt(m, key),'ECB'
    #CBC
    else:
        iv = random_key(16)
        return AES_CBC_H.encrypt(m, key, iv),'CBC'

if __name__ == '__main__':
    m=random_encrypto('this is a random encrypto!')
    print len(m[0])
    print m[1]