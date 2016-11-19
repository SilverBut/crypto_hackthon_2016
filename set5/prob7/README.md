## Problem 39.Implement RSA

### 0x01 Question
这题要求我们实现一个RSA加密。

### 0x02 Environment
* Python 3.5 with gmpy2,pycrypto,binascii

### 0x03 Step
1. 使用__Crypto.Util.number.getPrime(length)__函数来产生足够长的大素数。
2. 通过自己写的__egcd__以及__invmod__函数来找到合适的p使得`p*d=1(mod n)`。
3. 这里采用`binascii.hexlify(message.encode())`来获取明文的hex。
4. 对于大数的指数运算，这里使用了`gmpy2.powmod(number,exp,mod)`函数。
5. 最终的密文经过了__base64__加密。

### 0x04 More
* 实现RSA的时候出现了几个问题。首先是`m**e%n`这样的大数指数运算速度太慢。最后找到了`gmpy2.powmod`函数来解决。
* 因为一开始选择的素数长度不够，所以使用了`Crypto.Util.number.getPrime()`函数来取得需要位数的大素数。

### 0x05 Reference
[PyCrypto API Documentation](http://pythonhosted.org/pycrypto/)
[Gmpy2 API Documentation](http://gmpy2.readthedocs.io/en/latest)

