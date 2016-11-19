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
rsa_private = 0
rsa_p = 0
rsa_q = 0
print("Encrypt finished. Key thrown!")
# Normally, if we want to decrypt here, we need to do this:
#dec_data = rsa_lib.decrypt(enc_data, rsa_private, rsa_p, rsa_q)
#print(dec_data)
# However it is not possible now, since we've removed all related things
print("So now we can only relay on ourselves to decrypt it!")

print(type(enc_data))
