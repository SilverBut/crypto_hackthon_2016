#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from time import sleep
from urlparse import urlparse, parse_qs
import hashlib
import itertools
from stuff import hmac_sha1, raw2hex

def insecure_compare(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in xrange(len(str1)):
        if str1[i] != str2[i]:
            return False
        sleep(0.05)
    return True

def verify(val, sig):
    key = 'you will never guess my key'
    print '\n' + '=' * 0x20
    print 'hmac: ' + raw2hex(hmac_sha1(key, val))
    print 'sig : ' + raw2hex(sig.decode('hex'))
    print '=' * 0x20 + '\n'
    return insecure_compare(hmac_sha1(key, val), sig.decode('hex'))

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        filename, signature = query['file'][0], query['signature'][0]
        valid = verify(filename, signature)

        if not valid:
            self.send_response(500)
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header("Content-Type", 'application/octet-stream')
            self.end_headers()
            self.wfile.write(open(filename))

# main
if __name__ == '__main__':
    httpd = HTTPServer(('', 9000), MyHTTPRequestHandler)
    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()
