#!/usr/bin/python3
import hashlib

site_p = (0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1)

site_q = (0xf4f47f05794b256174bba6e9b396a7707e563c5b)

site_g = (0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291)

site_verify = "ca8f6f7c66fa362d40760d135b763eb8527d3d52"

def extended_gcd(a, b):
    s = 0;    old_s = 1
    t = 1;    old_t = 0
    r = b;    old_r = a
    while r != 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)
    return {"B":[old_s, old_t], "G":old_r, "Q":[t, s]}

def invmod(a, m):
    D = extended_gcd(a,m)
    if D['G'] != 1:
        raise Exception("a and m are not coprime. "
                        + str(a) + " " + str(m) + " " + str(D['G']))
    ans = D['B'][0]
    if ans < 0:
        ans += m
    return ans

assert invmod(17, 3120) == 2753

def read_data(filename="44.txt"):
    data=[]
    with open(filename, "r") as fp:
        while True:
            msg = fp.readline()[5:] # strip start 'msg: '
            if msg=='':
                break
            s   = fp.readline()[3:] # strip start 's: '
            r   = fp.readline()[3:] # strip start 'r: '
            m   = fp.readline()[3:] # strip start 'm: '
            # post process
            s   = int(s, 10)
            r   = int(r, 10)
            m   = int(m, 16)
            data.append({"msg":msg, "s":s, "r":r, "m":m})
    return data

def burp(data):
    # try to solve k out
    k = ((data[1]["m"] - data[0]["m"])*invmod(data[1]["s"] - data[0]["s"], site_q)) % site_q
    return k

if __name__=="__main__":
    data = read_data() # read input data
    # first find all pairs with same nonce
    # if they have same nonce, since r=g^k mod p mod q, they must have same r
    dangers = []
    for lhs_r in range(len(data)):
        lhs = data[lhs_r]
        target = ()
        x = lhs["r"]
        for rhs_r in range(lhs_r, len(data)):
            rhs = data[rhs_r]
            if rhs["r"] == x and rhs["msg"] != lhs["msg"] and rhs["s"] != lhs["s"]:
                target+=(rhs,)
        if len(target):
            target+=(lhs,)
            dangers.append(target)
    print("Found %d group of targets. Burping now..."%(len(dangers)))
    data = dangers[0] # just use 0 for a test
    
    nonce = burp(data)
    # and now we have all arguments except for private key. why not burp it like challenge 43;)?
    x=((data[0]["s"]*nonce-data[0]["m"]) * invmod(data[0]["r"],site_q))%site_q
    # and check with correct value
    print(x)

    m = hashlib.sha1()
    m.update(bytes(hex(x)[2:],'ascii'))
    print(m.hexdigest())
    if (m.hexdigest() == site_verify):
        print("Succeed.")
    else:
        print("GG")


