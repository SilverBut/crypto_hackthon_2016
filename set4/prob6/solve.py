#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from md4 import MD4
from stuff import raw2hex

# main
if __name__ == '__main__':
    m = MD4()
    m.update(raw2hex("test"))
    print m.digest()
    pass
