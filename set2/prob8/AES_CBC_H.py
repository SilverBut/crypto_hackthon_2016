__author__ = 'Administrator'
import AES_ECB,hex_xor,HexBase64


def decrypt(c, key, iv):
    m = ''
    if len(c) % 16 != 0:
        return
    else:
        for i in range(0, len(c)/16):
            pc=AES_ECB.decrypt(c[16*i:16*(i+1)], key)
            pc = hex_xor.hex_xor(iv.encode('hex'),pc.encode('hex')).decode('hex')
            m = m+pc
            iv= c[16*i:16*(i+1)]
        return m

def encrypt(m, key, iv):
    c=iv
    if len(m) % 16 != 0:
        return
    else:
        for i in range(0, len(m)/16):
            pc = hex_xor.hex_xor(iv.encode('hex'), m[16*i:16*(i+1)].encode('hex')).decode('hex')
            iv = AES_ECB.encrypt(pc, key)
            c = c+iv
        return c

if __name__ == '__main__':
    f = open('10.txt', 'r')
    c = HexBase64.base642hex(f.read()).decode('hex')
    key = 'YELLOW SUBMARINE'
    iv = chr(0)*16
    print decrypt(c, key, iv)
