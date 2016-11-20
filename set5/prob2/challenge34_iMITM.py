from Crypto.Hash import SHA
from challenge33_iDH import *
from Crypto.Cipher import AES
from Crypto.Random import random

print("p: "+str(p))
print("\ng: "+str(g))
print("\na: "+str(a))
print("\nb: "+str(b))
print("\nA: "+str(bigA))
print("\nB: "+str(bigB))

print("\ns: "+str(sa))

message="A"*16

iv=random.Random.get_random_bytes(16)

ea=AES.new(key[:16],AES.MODE_CBC,iv)
print("\n[Normal] A->B: ")
c=ea.encrypt(message)
message_a=c+iv
print(message_a)

print("\n[Normal] B decrypt: ")
da=AES.new(key[:16],AES.MODE_CBC,message_a[16:])
print(da.decrypt(message_a[:16]))

iv=random.Random.get_random_bytes(16)
eb=AES.new(key[:16],AES.MODE_CBC,iv)
print("\n[Normal] B->A: ")
message="B"*16
c=eb.encrypt(message)
message_b=c+iv
print(message_b)

print("\n[Normal] A decrypt: ")
db=AES.new(key[:16],AES.MODE_CBC,message_b[16:])
print(db.decrypt(message_b[:16]))

########MITM Start#######
###Share key###
print("######MIMT Start######")
print("[MITM] A->M: p, g, A")
#print("p: "+str(p))
#print("g: "+str(g))
#print("A: "+str(bigA))

print("[MITM] M->B: p, g, p")
#print("p: "+str(p))
#print("g: "+str(g))
#print("p: "+str(p))

print("[MITM] B->M: B")
#print("B: "+str(bigB))

print("[MITM] M->A: p")
#print("p: "+str(p))

print("\n[MITM] A has Key: (p ** a) % p")

print("[MITM] B has Key: (p ** b) % p")
print("[MITM] M has Key: \n(p ** a) % p\n(p ** b) % p\n(A ** b) % p")

###A->B###
print("\n[MITM] A->M:")
iv=random.Random.get_random_bytes(16)
k_a2m=SHA.new(str(pow(p,a,p)).encode()).digest()
e_a=AES.new(k_a2m[:16],AES.MODE_CBC,iv)
m_a="A"*16
message_a2m=e_a.encrypt(m_a.encode())+iv
print(message_a2m)

print("\n[MITM] M read message from A with key (p ** a) % p: ")
d_a2m=AES.new(k_a2m[:16],AES.MODE_CBC,message_a2m[16:])
p_a2m=d_a2m.decrypt(message_a2m[:16])
print(p_a2m.decode())
print("[MITM] And M pack this message with key (p ** b) % p and relay to B: ")
k_m2b=SHA.new(str(pow(p,b,p)).encode()).digest()
iv_m2b=random.Random.get_random_bytes(16)
e_m2b=AES.new(k_m2b[:16],AES.MODE_CBC,iv_m2b)
message_m2b=e_m2b.encrypt(p_a2m)+iv_m2b
print(message_m2b)

print("\n[MITM] B unpack message from M with key (p ** b) % p: ")
d_m2b=AES.new(k_m2b[:16],AES.MODE_CBC,message_m2b[16:])
p_m2b=d_m2b.decrypt(message_m2b[:16])
print(p_m2b)

###B->A###
print("\n[MITM] B->M: ")
iv_b2m=random.Random.get_random_bytes(16)
m_b2m="B"*16
k_b2m=SHA.new(str(pow(p,b,p)).encode()).digest()
e_b2m=AES.new(k_b2m[:16],AES.MODE_CBC,iv_b2m)
message_b2m=e_b2m.encrypt(m_b2m.encode())+iv_b2m
print(message_b2m)

print("\n[MITM] M unpack message from B with key (p ** b) % p: ")
d_b2m=AES.new(k_b2m[:16],AES.MODE_CBC,message_b2m[16:])
p_b2m=d_b2m.decrypt(message_b2m[:16])
print(p_b2m.decode())
print("[MITM] And M pack this message with key (p ** a) % p and relay to A: ")
iv_m2a=random.Random.get_random_bytes(16)
k_m2a=SHA.new(str(pow(p,a,p)).encode()).digest()
e_m2a=AES.new(k_m2a[:16],AES.MODE_CBC,iv_m2a)
message_m2a=e_m2a.encrypt(p_b2m)+iv_m2a
print(message_m2a)

print("\n[MITM] A unpack message from M with key (p ** b) % p: ")
d_m2a=AES.new(k_m2a[:16],AES.MODE_CBC,message_m2a[16:])
p_m2a=d_m2a.decrypt(message_m2a[:16])
print(p_m2a.decode())
