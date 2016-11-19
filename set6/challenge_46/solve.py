#!/usr/bin/python3
import rsa_lib
import base64
import hashlib

print("Hi. Here I'd introduce 'RSA Parity Oracle'")
print("First, let's encrypt some message with RSA. I'll try not to save the content, nor I will save the private key. ")

original_message = "VGhhdCdzIHdoeSBJIGZvdW5kIHlvdSBkb24ndCBwbGF5IGFyb3VuZCB3aXRoIHRoZSBGdW5reSBDb2xkIE1lZGluYQ=="

m = hashlib.md5()
m.update(base64.b64decode(original_message))
print("FYI, md5(orgininal_message) = %s"%(m.hexdigest()))

# Encrypting now! Install pycrypto if you got any error here
src_data = base64.b64decode(original_message)

rsa_n = 1024
rsa_p = rsa_lib.getPrime(rsa_n)
rsa_q = rsa_lib.getPrime(rsa_n)
rsa_public, rsa_private, rsa_mod = rsa_lib.genRSA(rsa_p, rsa_q)
enc_data = rsa_lib.encrypt(src_data, rsa_public, rsa_mod)
print("Encrypt finished. ")
# Normally, if we want to decrypt here, we need to do this:
#dec_data = rsa_lib.decrypt(enc_data, rsa_private, rsa_p, rsa_q)
#print(dec_data)
# However it is not possible now, since we've removed all related things
print("So now we can only relay on ourselves (and oracle) to decrypt it!")
print("Since the task is boring, we need to write a oracle first.")
print("Besides, a custom decrypt function is needed. Just wait a few more seconds...")

def oracle_isOdd(target, sk, p, q):
    mod = p*q
    size = rsa_lib.modSize(mod)
    output=""
    aux3 = target
    m1 = pow(aux3, sk%(p-1), p)
    m2 = pow(aux3, sk%(q-1), q)
    h = (rsa_lib.inv(q, p)*(m1-m2))%p
    aux4 = m2+h*q
    return aux4 & 0b1   # return True if is odd

print("Oracle prepared, let me try to decrypt it...")

# first calculate out mod size
size = rsa_lib.modSize(rsa_mod)
target_list = enc_data.copy()
up = rsa_mod
down = 0
while target_list:
    target_num = rsa_lib.list2Int(target_list[:size + 2])
    assert target_num < rsa_mod
    fac = pow(2, rsa_public, rsa_mod)
    while True:
        target_num *= fac
        if oracle_isOdd(target_num, rsa_private, rsa_p, rsa_q):
            # 2P > N
            down += (up-down)//2-1
        else:
            # 2P < N
            up -= (up-down)//2-1
        if ( up - down <= 26 ):
            break  # for fun...
    break
# for some problems with the RSA module, we need to brute force again
print("%x, %x"%(up, down))
if up < down:
    vup = down
    down =up
    up = vup
for val in range(down, up):
    tvx = rsa_lib.int2Text(val, 67)
    if src_data.decode() == tvx:
        print("Good! Got right text: %s"%(tvx))


