#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from sha1 import sha1
from os import urandom

def mac(key, data):
    return sha1(key + data)

def solve():
    key_raw = urandom(0x10)
    pt1_raw = "test1"
    pt2_raw = "test2"
    key_raw = b'YELLOW SUBMARINE'
    pt1_raw = b'Four Score And Seven Years Ago'
    pt2_raw = b'Four Score and Eight Years Ago'
    print mac(key_raw, pt1_raw)
    print mac(key_raw, pt2_raw)

# main
if __name__ == '__main__':
    solve()
