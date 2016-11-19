from md4 import MD4
import struct

def generateMD4Padding(message_length_in_bytes):
    return b'\x80' + (b'\x00' * ((56 - (message_length_in_bytes + 1) % 64) % 64)) + struct.pack('<Q', message_length_in_bytes*8)


hash_secret = b'YELLOW SUBMARINE'

def dumbMD4HashAuth(key, message):
    return MD4().update(key + message).digest()

def checkDumbHashAuth(message, tag):
    return (dumbMD4HashAuth(hash_secret, message) == tag)

def appendMessage(original, tag, extra):
    #assume secret is between 0 and 64 bytes in length
    for i in range(0, 65):
        oldpadding = generateMD4Padding(len(original)+i);
        newdata = extra;
        a = int.from_bytes(tag[0:4], byteorder='little');
        b = int.from_bytes(tag[4:8], byteorder='little');
        c = int.from_bytes(tag[8:12], byteorder='little');
        d = int.from_bytes(tag[12:16], byteorder='little');
        newtag = MD4(A=a, B=b, C=c, D=d, numbytes=i+len(original + oldpadding)).update(newdata).digest()
        if (checkDumbHashAuth(original + oldpadding + extra, newtag)):
            print(original + oldpadding + extra)
            return newtag
    print("Failure");


def test30():
    message = b'comment1=cooking%20MCs;userdata=foo;comment2=%20like%20a%20pound%20of%20bacon'
    print('message ' ,message)
    tag = dumbMD4HashAuth(hash_secret, message)
    print('hash(secret||message) ',tag)
    newtag = appendMessage(message, tag, b';admin=true');
    print("new tag = ", rawToHex(newtag))

if (__name__ == "__main__"):
    test30()
