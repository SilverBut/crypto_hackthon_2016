## Problem 33.Implement Diffie-Hellman
这题要求我们实现一个简单的DH。

### 0x01 Environment
* python3.5 with Crypto

### 0x02 Step
1. 首先，我们生成一个__NIST Prime__为`p`，且`g=2`。
2. 随机生成一个大数`a = rand % p`，并计算`A = (g**a) % p`。
3. 同样生成b与B。
4. 我们可以得到相同的密钥`S = (A ** b) % p = (B ** a) % p`，即双方可以得到一样的密钥。
5. 通过这秘钥来进一步交换公钥私钥。

### 0x03 Reference
[Crypto API Documentations](http://pythonhosted.org/pycrypto/)
