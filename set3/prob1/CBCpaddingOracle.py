__author__ = 'Administrator'
import random
import set2.AES_CBC_H,set2.R_ECB_CBC,set2.pkcs7

key=set2.R_ECB_CBC.random_key(16)
iv=set2.R_ECB_CBC.random_key(16)


def encrypto(m):
    return set2.AES_CBC_H.encrypt(set2.pkcs7.pkcs7(m,16),key,iv)


def checkCipher(c):
    try:
        c = set2.pkcs7.d_pkcs7(set2.AES_CBC_H.decrypt(c[16:],key,c[0:16]),16)
    except set2.pkcs7.PadError as e:
        return False
    return True

if __name__ == '__main__':
    f=open('17.txt','r')
    ss=f.readlines()
    s=ss[random.randint(0,len(ss)-1)].strip('\n')
    print checkCipher(encrypto(s))