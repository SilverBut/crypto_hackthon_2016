from Crypto.Hash import SHA
from Crypto.Util import number
from Crypto.Cipher import AES
from Crypto.Random import random

def genA(p, g, a):
    return pow(g,a,p)

def genS(A, b, p):
    return pow(A,b,p)

def genKey(s):
    return SHA.new(str(s).encode()).digest()

def printSend(stage, send, recv, string):
    print("\n["+stage+"] "+send+"->"+recv+": ")
    print(string)

def printRead(stage, reader, string):
    print("\n["+stage+"] "+reader+" recv message: "+string)

def genPrime():
    return number.getPrime(512)

def genNum(p):
    return random.randint(1,p)

def genIV():
    return random.Random.get_random_bytes(16)

def gFun(tag):
    p=genPrime()
    a=genNum(p)
    b=genNum(p)
    if(tag==1):
        g=1
        tag="G =1"
        message=tag*4
    elif(tag==2):
        g=p
        tag="G =p"
        message=tag*4
    else:
        g=p-1
        tag="G =p - 1"
        message=tag*2


    A=genA(p,g,a)
    B=genA(p,g,b)
    S=genS(A,b,p)
    K=genKey(S)
    
    print("\np: "+str(p))
    print("S: "+str(S))

    iv_a2b=genIV()
    message_a2b=AES.new(K[:16],AES.MODE_CBC,iv_a2b).encrypt(message)+iv_a2b
    printSend(tag,"A","B",message_a2b)
    
    p_a2b=AES.new(K[:16],AES.MODE_CBC,message_a2b[16:]).decrypt(message_a2b[:16])
    printRead(tag,"M",p_a2b.decode())
    printRead(tag,"B",p_a2b.decode())

    iv_b2a=genIV()
    message_b2a=AES.new(K[:16],AES.MODE_CBC,iv_b2a).encrypt(p_a2b)+iv_b2a
    printSend(tag,"B","A",message_b2a)

    p_b2a=AES.new(K[:16],AES.MODE_CBC,message_b2a[16:]).decrypt(message_b2a[:16])
    printRead(tag,"M",p_b2a.decode())
    printRead(tag,"A",p_b2a.decode())

def run():
    gFun(1)
    gFun(2)
    gFun(3)

if __name__ == "__main__":
    run()
