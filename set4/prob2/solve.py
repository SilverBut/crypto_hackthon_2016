#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import os
from stuff import aes_ctr_dec, aes_ctr_enc, pkcs7, del_pkcs7, repeat_xor

aes_ctr_enc_local = None
aes_ctr_dec_local = None

def find_subpt(ct_raw, subpt_raw):
    pt_raw = aes_ctr_dec_local()
    pass

# sub
def enc_custom(pre, suf, pt_raw):
    magic = pre + pt_raw.replace(";", "';'").replace("=", "'='") + suf
    return aes_ctr_enc_local(pkcs7((magic), 16))

def dec_custom(pre, suf, ct_cus_raw):
    magic = del_pkcs7(aes_ctr_dec_local(ct_cus_raw), 16)
    print magic
    return magic

# main
def do_enc(pre, suf, pt_raw):
    return enc_custom(pre, suf, pt_raw)

def do_dec_check(pre, suf, ct_cus_raw):
    magic = dec_custom(pre, suf, ct_cus_raw)
    if ";admin=true;" in magic:
        return True
    else:
        return False

def init():
    key_raw = os.urandom(16)
    iv_raw  = lambda : '\x00' * 0x10
    global aes_ctr_enc_local
    global aes_ctr_dec_local
    aes_ctr_enc_local = lambda raw_pt: aes_ctr_enc(raw_pt, key_raw, iv_raw)
    aes_ctr_dec_local = lambda raw_ct: aes_ctr_dec(raw_ct, key_raw, iv_raw)

def solve():
    init()
    pre_raw     = "comment1=cooking%20MCs;userdata="
    suf_raw     = ";comment2=%20like%20a%20pound%20of%20bacon"
    payload0    = "A" * (16 - len(pre_raw) % 16) + "\x00" * 0x10
    attacked    = len(pre_raw + payload0) // 0x10 - 1
    ct_cus_raw  = do_enc(pre_raw, suf_raw, payload0)

    # exploit
    attacked_keystream = ct_cus_raw[(attacked) * 0x10: (attacked + 1) * 0x10]
    target      = ";admin=true;AAAA"
    attacked_fi = repeat_xor(attacked_keystream, target)
    payload1    = (ct_cus_raw[:(attacked) * 0x10] +
                   attacked_fi +
                   ct_cus_raw[(attacked + 1) * 0x10:])

    # check result
    result      = do_dec_check(pre_raw, suf_raw, payload1)
    if result:
        print "congratz!:)"
    else:
        print "failed:("

# main
if __name__ == '__main__':
    solve()
