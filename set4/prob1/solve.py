#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from stuff import download, aes_ctr_enc, aes_ctr_dec, repeat_xor
import os

def get_api(key, counter):
    def edit(ct, offset, newtext):
        old_pt = aes_ctr_dec(ct, key, counter)
        new_pt = old_pt[:offset] + newtext + old_pt[offset+len(newtext):]
        new_ct = aes_ctr_enc(new_pt, key, counter)
        return new_ct
    return edit

def break_random_access_ctr(ct_raw, edit_api):
    key_stream_raw = edit_api(ct_raw, 0x0, '\x00' * len(ct_raw))
    pt_raw = repeat_xor(key_stream_raw, ct_raw)
    print pt_raw

def solve():
    with open('./text', 'r') as fp:
        pt_raw = fp.read()
    key_raw = os.urandom(16)
    counter = lambda : '\x00' * 0x10
    edit_api = get_api(key_raw, counter)
    ct_raw = aes_ctr_enc(pt_raw, key_raw, counter)
    break_random_access_ctr(ct_raw, edit_api)

# main
if __name__ == '__main__':
    solve()
