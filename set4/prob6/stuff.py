#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import base64
from Crypto.Cipher import AES

"""
utils for string processing

example:
    raw     : "AAAA"
    ascs    : [0x41, 0x41, 0x41, 0x41]
    hex     : "41414141"
"""

# stuff
hex2raw     = lambda h: h.decode('hex')
raw2hex     = lambda h: h.encode('hex')

hex2ascs    = lambda h: [ord(ch) for ch in h.decode('hex')]
ascs2hex    = lambda ascs: ''.join([chr(o) for o in ascs]).encode('hex')

raw2ascs    = lambda raw: [ord(ch) for ch in raw]
ascs2raw    = lambda ascs: ''.join([chr(h) for h in ascs])

b642raw     = lambda b64: base64.b64decode(b64)
raw2b64     = lambda b64: b64encode(b64)

# aes mode
def aes_ecb_enc(pt_raw, key_raw):
    aes = AES.new(key_raw, AES.MODE_ECB)
    return aes.decrypt(pt_raw)
def aes_ecb_dec(ct_raw, key_raw):
    aes = AES.new(key_raw, AES.MODE_ECB)
    return aes.decrypt(ct_raw)
def aes_cbc_enc(ct_raw, key_raw, iv_raw):
    aes = AES.new(key_raw, AES.MODE_CBC, iv_raw)
    return aes.encrypt(ct_raw)
def aes_cbc_dec(ct_raw, key_raw, iv_raw):
    aes = AES.new(key_raw, AES.MODE_CBC, iv_raw)
    return aes.decrypt(ct_raw)
def aes_ctr_enc(pt_raw, key_raw, counter):
    aes     = AES.new(b'YELLOW SUBMARINE', AES.MODE_CTR, counter=counter)
    ct_raw  = aes.encrypt(pt_raw)
    return ct_raw
def aes_ctr_dec(ct_raw, key_raw, counter):
    aes     = AES.new(b'YELLOW SUBMARINE', AES.MODE_CTR, counter=counter)
    pt_raw  = aes.decrypt(ct_raw)
    return pt_raw

# PKCS#7 padding
def pkcs7(raw, block):
    pad_num = block - (len(raw) % block)
    return raw + pad_num * chr(pad_num)
def del_pkcs7(raw, block):
    if len(raw) % block == 0:
        return raw
    else:
        pad_num = ord(raw[-1])
        ori_len = len(raw) - pad_num
        for i in xrange(pad_num):
            if raw[ori_len + i] != chr(pad_num):
                return None
        return raw[:ord(raw[-1])]

# return array of raw string
def download(fn):
    with open(fn, 'r') as fp:
        lines = []
        while True:
            line = fp.readline().strip()
            if not line:
                break
            lines.append(line)
        return lines

# check whether a raw string is printable
def check_printable(s):
    flag = True
    for i in xrange(len(s)):
        stuff = s[i]
        if ord(stuff) >= 0x41 and ord(stuff) <= 0x5a:
            pass
        elif ord(stuff) >= 0x61 and ord(stuff) <= 0x7a:
            pass
        elif ord(stuff) <= 0x40 and ord(stuff) >= 0x20:
            pass
        elif ord(stuff) == 0xa:
            pass
        else:
            flag = False
    return flag

# input a raw pt and raw key, output repeating xor'd raw ct
def repeat_xor(raw_pt ,raw_key):
    ascs_plain = raw2ascs(raw_pt)
    ascs_key = raw2ascs(raw_key)
    result = []
    len_plain = len(raw_pt)
    len_key = len(raw_key)
    len_res = len_plain % len_key
    for i in xrange(0, len_plain-len_res, len_key):
        for j in xrange(0, len_key):
            result.append(ascs_plain[i+j] ^ ascs_key[j])
    for i in xrange(0, len_res):
        result.append(ascs_plain[(len_plain-len_res) + i] ^ ascs_key[i])
    return ascs2raw(result)

# compute Hamming Distance of two raw string
def hamming_distance(raw_pt1, raw_pt2):
    assert len(raw_pt1) == len(raw_pt2)
    ascs_pt1 = raw2ascs(raw_pt1)
    ascs_pt2 = raw2ascs(raw_pt2)
    hm = 0
    for i in xrange(len(raw_pt1)):
        stuff1 = ascs_pt1[i]
        stuff2 = ascs_pt2[i]
        stuff = stuff1 ^ stuff2
        for i in xrange(0x8):
           hm = hm + ((stuff & (0x1<<i)) >> i)
    return hm


