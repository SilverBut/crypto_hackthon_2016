#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from sha1 import Sha1Hash, sha1
from os import urandom
from stuff import raw2hex, hex2raw
import struct

key_raw = urandom(0x10)
key_raw = b'YELLOW SUBMARINE'

def check(data, tag):
    gen_tag = sha1(key_raw + data)
    return (gen_tag == tag)

def gen_sha1_padding(data_len):
    return ('\x80' +
            ('\x00' * ((56 - (data_len + 1) % 64) % 64)) +
            struct.pack('>Q', data_len * 8))

def sha1_hash_no_padding(data, h):
    return '%08x%08x%08x%08x%08x' % Sha1Hash(h).update(data)._h

def hash_extend_attack(old_message, old_tag, new_message):
    # try key length
    for i in xrange(100):
        old_pad = gen_sha1_padding(len(old_message) + i)
        new_pad = gen_sha1_padding(len(old_message) + len(old_pad) + len(new_message)
                                 + i)
        new_data = new_message + new_pad
        a = struct.unpack(">I", (old_tag[0:4]))[0]
        b = struct.unpack(">I", (old_tag[4:8]))[0]
        c = struct.unpack(">I", (old_tag[8:12]))[0]
        d = struct.unpack(">I", (old_tag[12:16]))[0]
        e = struct.unpack(">I", (old_tag[16:20]))[0]
        new_tag = sha1_hash_no_padding(new_data, (a, b, c, d, e))
        if check(old_message + old_pad + new_message, new_tag):
            print "congratz!"
            return new_tag
    print "failed"

def solve():
    old_message = ("comment1=cooking%20MCs;"
                   "userdata=foo;comment2=%"
                   "20like%20a%20pound%20of"
                   "%20bacon")
    old_tag = sha1(key_raw + old_message)
    print "[+] original tag : {}".format(old_tag)
    new_data = ";admin=true"
    new_tag = hash_extend_attack(old_message, hex2raw(old_tag), new_data)
    print '[+] new tag      : {}'.format(new_tag)

# main
if __name__ == '__main__':
    solve()
    pass

