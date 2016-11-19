#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import requests
from stuff import raw2hex
import time

def set_byte(s, i, ch):
    return s[:i] + ch + s[i+1:]
def attack_request(f, sig):
    url     = ('http://localhost:9000/test?file=' + f +
               '&signature=' + raw2hex(sig))
    start   = time.time()
    requests.get(url)
    stop    = time.time()
    return stop - start

def check(text, index, mac, current_timing):
    count = 0x0
    for i in xrange(0x100):
        mac = set_byte(mac, index, chr(i))
        timing = attack_request(text, mac)
        delta = timing - current_timing
        if delta < 0.03 and delta > -0.03:
            count += 1
    print count
    if count >= 0xe0:
        return True
    else:
        return False

def leak_byte(text, index, mac, current_timing):
    final_timing = []
    for i in xrange(0x100):
        if index == 19:
            mac = set_byte(mac, index, chr(i))
            timing = attack_request(text, mac)
            delta = timing - current_timing
            if delta < 0.02 and delta > -0.02:
                final_timing.append(i)
                continue
            elif i == 0xff:
                return final_timing
            else:
                continue
        mac = set_byte(mac, index, chr(i))
        timing = attack_request(text, mac)
        delta = timing - current_timing
        if delta < 0.02 and delta > -0.02:
            mac_tmp = set_byte(mac, index + 1, chr(i))
            if check(text, index+1, mac_tmp, current_timing):
                return chr(i)
    print 'again'
    return None

def leak_hmac_sha1(text):
    mac = '\x00' * 20
    for i in xrange(19):
        leaked = None
        current_timing = 0.05 * (i+1)
        while not leaked:
            leaked = leak_byte(text, i, mac, current_timing)
        mac = set_byte(mac, i, leaked)
        print '[+] %dth byte leaked! current MAC: '%(i+1) + raw2hex(mac)
    current_timing = 0.05 * (19+1)
    leaked = leak_byte(text, 19, mac, current_timing)
    print '[+] %dth byte leaked! candidate val: '%20 + ''.join(['%x '%val for val in leaked])

# main
if __name__ == '__main__':
    leak_hmac_sha1("foo")
    pass
