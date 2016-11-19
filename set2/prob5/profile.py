__author__ = 'Administrator'
import R_ECB_CBC
import Crypto.Cipher.AES
import pkcs7


def profile_for(m):
    m=m.replace('&','')
    m=m.replace('=','')
    m='email='+m+'&uid=10&role=user'
    return m


key=R_ECB_CBC.random_key(16)
def encryptrandom(m):
    iv=R_ECB_CBC.random_key(16)
    cryptor=Crypto.Cipher.AES.new(key,Crypto.Cipher.AES.MODE_CBC,iv)
    return iv+cryptor.encrypt(m)

def decryptpro(c):
    cryptor=Crypto.Cipher.AES.new(key,Crypto.Cipher.AES.MODE_CBC,c[0:16])
    return cryptor.decrypt(c[16:])

def parseprofile(m):
    ms=m.split('&')
    ms[0]=ms[0].split('email=')[1]
    ml={'emali:':ms[0],'uid:':ms[1],'role:':ms[2]}
    return ml

if __name__ == '__main__':
    emali='foo@bar.com'
    #email='foo@bar.com&role=admin'
    pf=profile_for(emali)
    print pf
    c=encryptrandom(pkcs7.pkcs7(pf, 16))
    print c
    pf=decryptpro(c)
    ms=parseprofile(pf)
    for key in ms:
        print key,ms[key]
    s='\"provide\" that to the \"attacker\"'
    print len(s)
