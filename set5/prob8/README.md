#Problem 40.Implement an E=3 RSA Broadcast attack
Implement an E=3 RSA Broadcast attack

### 0x01 Question
同一个e对同一明文加密三次，从获取到的这三个密文、公钥还原出明文

### 0x02 Step
compute the nth root of x
```
def find_invpow(x,n):
```
运用中国剩余定理求message
```
c0, c1, c2 = [c % n for c,n in zip(cipher, public_key)]
n0, n1, n2 = public_key
ms0 = n1 * n2
ms1 = n0 * n2
ms2 = n0 * n1
N012 = n0 * n1 * n2
result = ((c0 * ms0 * modinv(ms0, n0)) +
        (c1 * ms1 * modinv(ms1, n1)) +
        (c2 * ms2 * modinv(ms2, n2))) % N012

mseeage = find_invpow(result, e)
```

### 0x03 the Point
使用CRT算法恢复明文

### 0x04 Reference
[CRT](http://www.di-mgt.com.au/crt_rsa.html)
[中国剩余定理](https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%9B%BD%E5%89%A9%E4%BD%99%E5%AE%9A%E7%90%86)
[Modular\_inverse](https://rosettacode.org/wiki/Modular_inverse)
[How to compute the nth root of a very big integer](http://218.193.131.250:8426/?query=nth-root&intent=1)
