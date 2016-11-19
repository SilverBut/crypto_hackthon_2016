import random,binascii,base64
from gmpy2 import powmod
from Crypto.Util import number

def egcd(a, b):
    if(a==0):
        return (b,0,1)
    else:
        g,y,x=egcd(b%a,a)
        return (g,x-(b//a)*y,y)

def invmod(e, et):
    g,x,y=egcd(e,et)
    if(g!=1):
        return False
    else:
        return x%et

def genD():
    length=1024
    p=number.getPrime(length)
    q=number.getPrime(length)
    n=q*p
    et=(p-1)*(q-1)
    e=3
    d=invmod(e,et)

    return (e,d,n)


def genKey():
    (e,d,n)=genD()
    while(d==False):
        (e,d,n)=genD()

    return ([e,n],[d,n])

def encrypt(message, public_key):
    temp=binascii.hexlify(message.encode())
    temp=int(temp,16)
    temp=powmod(temp,public_key[0],public_key[1])
    temp=int(temp.digits())
    temp=hex(temp)[2:]
    if(len(temp)%2!=0):
        temp='0'+temp
    temp=base64.b64encode(temp.encode())
    return temp.decode()

def decrypt(cipher, private_key):
    temp=base64.b64decode(cipher.encode())
    temp=int(temp,16)
    temp=powmod(temp,private_key[0],private_key[1])
    temp=int(temp.digits())
    temp=hex(temp)[2:]
    if(len(temp)%2!=0):
        temp='0'+temp
    temp=binascii.unhexlify(temp.encode())
    return temp.decode()

def run():
    (public_key,private_key)=genKey()

    print("Public Key:\ne: "+str(public_key[0])+"\nn: "+str(public_key[1]))
    print("\nPrivate Key:\nd: "+str(private_key[0])+"\nn: "+str(private_key[1]))

    print("\n\nPlease input a string:")
    message=input()
    cipher=encrypt(message,public_key)
    print("\nCipher: "+cipher)
    plain=decrypt(cipher,private_key)
    print("\nPlain: "+plain)

if __name__=="__main__":
    run()
