#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-

from md4 import MD4
from os import urandom
import struct
import codecs

key_raw = urandom(0x10)
key_raw = b'YELLOW SUBMARINE'

hex2raw     = lambda h: codecs.decode(h, 'hex')
raw2hex     = lambda h: codecs.encode(h, 'hex')

def md4(data):
    return MD4().update(data).digest()

def check(data, tag):
    gen_tag = md4(key_raw + data)
    return (gen_tag == tag)

def gen_md4_padding(data_len):
    return (b'\x80' +
            (b'\x00' * ((56 - (data_len + 1) % 64) % 64)) +
            struct.pack('<Q', data_len * 8))

def hash_extend_attack(old_message, old_tag, new_message):
    # try key length
    for i in range(17):
        old_pad = gen_md4_padding(len(old_message) + i)

        new_data = new_message
        a = struct.unpack("<I", (old_tag[0:4]))[0]
        b = struct.unpack("<I", (old_tag[4:8]))[0]
        c = struct.unpack("<I", (old_tag[8:12]))[0]
        d = struct.unpack("<I", (old_tag[12:16]))[0]
        new_tag = MD4(A=a, B=b, C=c, D=d, numbytes=i+len(old_message +
                                                         old_pad)
                     ).update(new_data).digest()
        if check(old_message + old_pad + new_message, new_tag):
            print("congratz!")
            return new_tag
    print("failed")

def solve():
    old_message = (b"comment1=cooking%20MCs;"
                   b"userdata=foo;comment2=%"
                   b"20like%20a%20pound%20of"
                   b"%20bacon")
    old_tag = md4(key_raw + old_message)
    print("[+] original tag : {}".format(raw2hex(old_tag)))
    new_data = b";admin=true"
    new_tag = hash_extend_attack(old_message, old_tag, new_data)
    print('[+] new tag      : {}'.format(raw2hex(new_tag)))

# main
if __name__ == '__main__':
    solve()
    pass

