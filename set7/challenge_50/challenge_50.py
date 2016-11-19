from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
import binascii
import itertools
import string
import util

def CBC_Mac(passsword,iv,plain):     #return the vaule of the CMAC
    cipher = AES.new(d,AES.MODE_CBC,iv)
    c = cipher.encrypt(util.padPKCS7(plain, 16))
    return c[-16:]
                                     #original CMAC HASH 296b8d7cb78a243dda4d0a61d33bbdd1
def Collide(before,after):
    afterHash = CBC_Mac(b'YELLOW SUBMARINE',b'\x00'*16,after)
    padded = util.padPKCS7(after, 16)
    return padded + strxor(before[:16], afterHash) + before[16:]
                                     #variale length CMAC vul, like the Challenge 49

def CollidePrintable(before, after):   
    numFreeBytes = (7 - len(after)) % 16
    if numFreeBytes == 0:            #collision part
        numFreeBytes = 16
    for freeBytes in itertools.product(range(32, 127), repeat=numFreeBytes):
        padded = after + bytes(freeBytes)
        collision = Collide(before, padded)
        scrambledBytes = collision[-len(before):-len(before) + 16]
        if all(c >= 32 and c < 127 for c in scrambledBytes):
            return collision
if __name__ == '__main__':
    before = b"alert('MZA who was that?');\n"    #the original JS snippet to collide
    bHash = CBC_Mac(b'YELLOW SUBMARINE',b'\x00'*16,before)   #CBC_MAC algorithm
    print(binascii.hexlify(bHash))                          #show the result

    after = b"alert('Ayo, the Wu is back!'); //"       #the collide JS with anntotaion to cunstruct the same hash
    collision = CollidePrintable(before, after)        #call the CollisionPrintable function 
    print(collision, binascii.hexlify(CBC_Mac(b'YELLOW SUBMARINE',b'\x00'*16,collision)))
