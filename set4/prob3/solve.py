#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import os
from stuff import aes_cbc_dec, aes_cbc_enc, pkcs7, del_pkcs7, repeat_xor, raw2hex

aes_cbc_enc_local = None
aes_cbc_dec_local = None

# sub
def enc_custom(pre, suf, pt_raw):
    magic = pre + pt_raw.replace(";", "';'").replace("=", "'='") + suf
    return aes_cbc_enc_local(pkcs7((magic), 16))

def dec_custom(pre, suf, ct_cus_raw):
    magic = del_pkcs7(aes_cbc_dec_local(ct_cus_raw), 16)
    return magic

# main
def do_enc(pre, suf, pt_raw):
    return enc_custom(pre, suf, pt_raw)

def do_dec_check(pre, suf, ct_cus_raw):
    magic = dec_custom(pre, suf, ct_cus_raw)
    for ch in magic:
        if ord(ch) >= 0x80:
            return (False, '')
        else:
            return (True, magic)

def init():
    key_raw = os.urandom(16)
    iv_raw  = key_raw
    global aes_cbc_enc_local
    global aes_cbc_dec_local
    aes_cbc_enc_local = lambda raw_pt: aes_cbc_enc(raw_pt, key_raw, iv_raw)
    aes_cbc_dec_local = lambda raw_ct: aes_cbc_dec(raw_ct, key_raw, iv_raw)
    return key_raw

def solve():
    key_raw = init()
    pre_raw     = ""
    suf_raw     = ""
    pt1_raw     = "A" * 0x10
    pt2_raw     = "B" * 0x10
    pt3_raw     = "C" * 0x10
    payload0    = pt1_raw + pt2_raw + pt3_raw
    ct_cus_raw  = do_enc(pre_raw, suf_raw, payload0)

    # exploit
    payload1    = (ct_cus_raw[:0x10] +
                   "\x00"* 0x10 +
                   ct_cus_raw[:0x10])

    # receiver check result
    res, recov  = do_dec_check(pre_raw, suf_raw, payload1)
    if res:
        recoved_key_raw = repeat_xor(recov[:0x10], recov[0x20:0x30])
        print "[+] recovered key : {}".format(raw2hex(recoved_key_raw))
        print "[+] real key      : {}".format(raw2hex(key_raw))
        if recoved_key_raw == key_raw:
            print "congratz!:)"
        else:
            print "failed:("
    else:
        print "failed:("
# main
if __name__ == '__main__':
    solve()
