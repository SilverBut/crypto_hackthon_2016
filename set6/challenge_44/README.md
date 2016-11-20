# Problem 43

## 0x01 Question

It's required that, if you want to sign any messages using DSA, you are NOT allowed to use the same nonce (k) again, unless you want to fuck yourself and leak your pants.

## 0x02 Steps

You need to get the 44.txt from the site and process the data correctly.

It's known that `r=g^k mod p mod q`, and `g, p, q` are kept same. So if two messages have same `r` after signed, they are using the same k. Since we have `s = k^-1(H+xr)mod q`, then it is possible to solve k out by `k = (s2-s1)^-1 (H2-H1) mod q`. 

And since we have `s, k, r, q, H`, it is quite easy to solve `x`, which means private key. 

## 0x03 What's the point

This is useful if you happened to met some inperfect things...

## 0x04 Reference
