# Problem 43

Note: This program works under Python3. You may need to install `gmpy2` first.

## 0x01 Question

Consider a DSA algo with protocol params (p,q,g), public key (y) and sign result (r,s) known. Now we want you to solve the private key (x) out. The nonce (k) values between 0 and 2e16.

## 0x02 Steps

Brute force is easy enough since the k value is not very big.

It's known that
```
       (s * k) - H(msg)
  x = ----------------  mod q
              r
```

and 
```
r = (g^k mod p) mod q
s = (k^-1)(H(m)+x*r) mod q
```

First one can be used to brute k out, and since the problem already gave us a hash value, we can use it to verify k.

`solve.py` will give you the result.

## 0x03 What's the point

## 0x04 Reference
