#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from Crypto.Util.number import getPrime
from hashlib import sha1 as SHA1
from stuff import raw2hex

from gmpy2 import mpz
from gmpy2 import powmod
from gmpy2 import div

# pip install primefac
import primefac

from itertools import combinations

from random import randint

from ntheory import chinese_remainder_theorem

# from chinese import chinese

# p : modula
# q : vuln order (not the real order)
# g : generator
# x : secret key of Bob
# y : secret key of Alice
p = mpz(7199773997391911030609999317773941274322764333428698921736339643928346453700085358802973900485592910475480089726140708102474957429903531369589969318716771)
q = mpz(236234353446506858198510045061214171961)
g = mpz(4565356397095740655436854503483826832136106141639563487732438195343690437606117828318042418238184896212352329118608100083187535033402010599512641674644143)
j = (p - 1) / q
x = getPrime(1024)
y = getPrime(1024)

def multi_custom(x):
    multi = 1
    for i in x:
        multi *= i
    return multi

def mac(key, msg):
    sha1 = SHA1()
    sha1.update(key + msg)
    # raw
    return sha1.digest()

def dh():
    A   = pow(g, x, p)
    B   = pow(g, y, p)
    X = pow(bigB, a, p)
    Y = pow(bigA, b, p)

    if x == y:
        print("true")
    else:
        print("false")

# step1

i = 4
# all prime factors of j
# factors = list(primefac.primefac(j))
# print '\n'.join(map(str, factors))
j_victim = (2, 3, 3, 5, 109, 8539, 20641, 51977, 38833, 57529, 7963, 46337, 54319,
            39341, 96142199, 46323892554437, 534232641372537546151,
            80913087354323463709999234471)
# j_victim = (2, 3, 5, 109, 654, 1635, 3270, 8539, 20641, 51234, 51977, 38833, 41282, 42695, 57529,
#             7963,  46337, 54319, 39341,79630, 85390, 103205, 103954,116499,
#             123846,128085,  155931,162957, 172587,196705, 238890, 259885,
#             930751,1164990, 256170, 1559310, 2249869)
def step1():
    global i
    r = j_victim[i]
    i += 1
    print '[+] r  : '.ljust(0x10, ' ') + '%d' % r
    return r

# def find_j():
#     for comb in xrange(0, len(j_victim)):
#         j_combs = list(combinations(j_victim, comb + 1))
#         for j_comb in j_combs:
#             tmp = reduce(lambda x, y : x *y % p, j_comb)
#             if powmod(g, tmp, p):
#                 pass

# step2
def step2(r):
    h = powmod(randint(1, p), (p-1)/r, p)
    print '[+] h  : '.ljust(0x10, ' ') + '%d' % h
    return h

def step3(h):
    K = powmod(h, x, p)
    print '[+] K  : '.ljust(0x10, ' ') + '%d' % K
    return K

int2hex = lambda i: (len('%x'%i) % 2) * '0' + '%x'%i 

def step4(K):
    m = "crazy flamboyant for the rap enjoyment"
    t = mac((int2hex(K)).decode('hex'), m)
    print '[+] m  : '.ljust(0x10, ' ') + '%s' % m
    print '[+] t  : '.ljust(0x10, ' ') + '%s' % raw2hex(t)
    return (m, t)

def check(tag, msg, k_brute_forced):
    new_tag = mac((int2hex(k_brute_forced)).decode('hex'), msg)
    # print '[+] try tag  : '.ljust(0x10, ' ') + '%s' % raw2hex(new_tag)
    if tag == new_tag:
        return True
    else:
        return False

def step5(h, r, m, t):
    print '[!] begin brute force K' 
    for i in xrange(r):
        K_tmp = powmod(h, i, p)
        # print '%d' % i + ' ',
        if check(t, m, K_tmp):
            x_found = i%r
            print '[+] find x  : '.ljust(0x10, ' ') + '%d' % x_found
            return x_found
    return None

def try_try():
    r       = step1()  # eve do this
    h       = step2(r) # eve do this, send h to bob, bob will use it as A

    K       = step3(h) # bob do this , K: which we don't know
    m, t    = step4(K) # bob do this, use K to calculate mac, eve will get m and t

    # eve do this to find x
    x_found = step5(h, r, m, t)
    if x_found:
        print 'found bob\'s secret key x: %d' % x_found
        return (x, r)
    else :
        print 'failed to find x:('

# main
def solve():
    res = [(mpz(1), mpz(1))]
    while multi_custom(list(map(lambda x:x[1], res))) < q:
        res.append(try_try())
        print '[+] q  : '.ljust(0x10, ' ') + '%d' % q
        print '[+] pro: '.ljust(0x10, ' ') + '%d' % multi_custom(list(map(lambda x:x[1], res)))
        # print reduce(lambda x, y: x[1]*y[1], res)
    res = sorted(res[1:], key=lambda x:x[1])
    r_arr = list(map(lambda x: x[1], res))
    x_arr = list(map(lambda x: x[0]%x[1], res))

    print 'mod %d' % multi_custom(list(map(lambda x:x, r_arr)))
    print '[+] bob\'s secret : %d' % x
    a, n = chinese_remainder_theorem(res)
    print '[!] find secret %d mod %d' % (a, n)

if __name__ == '__main__':
    # factors = list(primefac.primefac(j))
    # print '\n'.join(map(str, factors))
    solve()

