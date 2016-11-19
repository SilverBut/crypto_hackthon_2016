__author__ = 'Administrator'
import random
import AES_CBC_H,R_ECB_CBC,pkcs7

key=R_ECB_CBC.random_key(16)
iv=R_ECB_CBC.random_key(16)


def encrypto(m):
    return AES_CBC_H.encrypt(pkcs7.pkcs7(m,16),key,iv)


def checkCipher(c):
    try:
        c = pkcs7.d_pkcs7(AES_CBC_H.decrypt(c[16:],key,c[0:16]),16)
    except pkcs7.PadError as e:
        return False
    return True

if __name__ == '__main__':
    f=open('17.txt','r')
    ss=f.readlines()
    s=ss[random.randint(0,len(ss)-1)].strip('\n')
    print checkCipher(encrypto(s))