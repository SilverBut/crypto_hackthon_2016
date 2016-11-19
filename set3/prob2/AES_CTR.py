__author__ = 'Administrator'
import AES_ECB
import hex_xor
import HexBase64

def crypt(c,key,nonce):
    m=''
    for i in xrange(0,len(c)/32+1):
        aesxor=AES_ECB.encrypt(nonce.decode('hex'),key).encode('hex')
        m += hex_xor.hex_xor(c[32*i:32*(i+1)],aesxor)
        nonce=increase_nonce(nonce)
    return m

def increase_nonce(nonce):
    ctr=0
    j=1
    for i in xrange(16,32,2):
        ctr+=int(nonce[i:i+2],16)*j
        j*=256
    ctr=(ctr+1)%(256^8)
    m=''
    for i in xrange(0,8):
        m+=chr(ctr%256).encode('hex')
        ctr=ctr/256
    return nonce[0:16]+m

if __name__ == '__main__':
    c=HexBase64.base642hex('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')
    key='YELLOW SUBMARINE'
    nonce='00'*16
    print crypt(c,key,nonce).decode('hex')