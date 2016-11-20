# Problem 46

## 0x01 Question

Just another padding oracle.

## 0x02 Steps

Have a revision of the RSA. To encrypt the text, you will calculate `c mod n == m^e mod n`, c for cipher text, m for original message and (n,e) pair for public key. 

That means this expression `c*(2**e mod n) mod n == (2*m)^e mod n == m^e mod n` is also right. Which means, if we product cipher text 'c' with '2\*\*e mod n', the new decrypted message dM is mod N of the production of the original m with 2. Obviously, N mod 2 is 1, so if the original m is larger than N/2, which means 2m\>N, and it means dM will certainly be a odd number. Combine this theory with binary search, you can find out the value of m.

## 0x03 What's the point

You need to type fast to make your code run faster ;)

## 0x04 Reference

RSA lib modified from this address:
 https://jhafranco.com/2012/01/29/rsa-implementation-in-python/
