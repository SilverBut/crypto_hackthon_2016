#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from stuff import aes_ctr_enc
from Crypto.Cipher import ARC4
import zlib
import os

key_raw = "You Will Not Guess The Key"

def format_request(msg):
    return ('POST / HTTP/1.1\n'
            'Host: hapless.com\n'
            'Cookie:'
            'sessionid=TmV2ZXIgcmV2ZWFsIHRoZSBXdS1UYW5nIFNlY3JldCE=\n' +
            'Content-Length: %d\n' % len(msg) +
            '%s'  % msg)

def compress(msg):
    return zlib.compress(msg)

def encrypt(msg):
    cipher = ARC4.new(key_raw)
    return cipher.encrypt(msg)

def oracle(msg):
    return len(encrypt(compress(format_request(msg))))

b64_charset = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
               'abcdefghijklmnopqrstuvwxyz'
               '0123456789+/')

def solve():
    guess_sessionid = ''
    for i in xrange(21):
        tmp_len = []
        for j in xrange(64):
            for k in xrange(64):
                tmp_len.append(oracle('Cookie:sessionid=' + guess_sessionid +
                                      b64_charset[k] + b64_charset[j]))
        guess_sessionid += (b64_charset[tmp_len.index(min(tmp_len)) % 64] +
                            b64_charset[tmp_len.index(min(tmp_len)) // 64])
    tmp_len = []
    for j in xrange(64):
        tmp_len.append(oracle('Cookie:sessionid=' + guess_sessionid + b64_charset[j]))
    guess_sessionid += b64_charset[tmp_len.index(min(tmp_len))]

    print '[+] recovered session id : %s' % (guess_sessionid + '=')

# main
if __name__ == '__main__':
    solve()
