
__author__ = 'Administrator'
import Crypto.Cipher.AES
import set1.HexBase64

def decrypt(c,key):
    encryptor=Crypto.Cipher.AES.new(key,Crypto.Cipher.AES.MODE_ECB)
    return encryptor.decrypt(c)

def encrypt(m,key):
    encryptor=Crypto.Cipher.AES.new(key,Crypto.Cipher.AES.MODE_ECB)
    return encryptor.encrypt(m)

if __name__ == '__main__':
    f=open('7.txt','r')
    c=set1.HexBase64.base642hex(f.read()).decode('hex')
    key='YELLOW SUBMARINE'
    print decrypt(c,key)