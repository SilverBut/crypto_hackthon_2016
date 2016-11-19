__author__ = 'Administrator'
import R_ECB_CBC,AES_CBC_H,pkcs7
import hex_xor

pre = "comment1=cooking%20MCs;userdata="
last = ";comment2=%20like%20a%20pound%20of%20bacon"
key = R_ECB_CBC.random_key(16)
iv = R_ECB_CBC.random_key(16)


def encrypto(s):
    return AES_CBC_H.encrypt(pkcs7.pkcs7(pre+s+last,16),key,iv)

def findadmin(c):
    m=AES_CBC_H.decrypt(c[16:],key,c[0:16])
    all=m.split(';')
    if 'admin=true' in all:
        return True
    else:
        return False

def modifycipher(c):
    l=len(pre)
    m='%20MCs;userdata='.encode('hex')
    cm=';admin=true;aaaa'.encode('hex')
    cm=hex_xor.hex_xor(m,cm)
    return c[0:16]+hex_xor.hex_xor(c[16:32].encode('hex'),cm).decode('hex')+c[32:]

if __name__ == '__main__':
    a = 1
    s = raw_input('please input')
    print findadmin(encrypto(s))
    print findadmin(modifycipher(encrypto(s)))
