## Problem 10<problem id>. the cryptopals crypto challenges

### 0x01 Question
CBC模式是一个块密码模式，可以帮助我们加密大小不一的消息。

此题要求我们解密10.txt，它用“YELLOW SUBMARINE” 加密，且在IV为ASCII 0的CBC模式下

### 0x02 Step (main code)
由于set1中写了很多工具类都可以用到此题。。请把这些import进来 别再issue了TT
```
import set1.AES_ECB,set1.hex_xor,set1.HexBase64
```
这些也在set1中详细解释过

本题解密过程如下：
```python
def decrypt(c, key, iv):
    m = ''
    if len(c) % 16 != 0:
        return
    else:
        for i in range(0, len(c)/16):
            pc=set1.AES_ECB.decrypt(c[16*i:16*(i+1)], key)
            pc = set1.hex_xor.hex_xor(iv.encode('hex'),pc.encode('hex')).decode('hex')
            m = m+pc
            iv= c[16*i:16*(i+1)]
        return m
```
顺手写了加密：
```python
def encrypt(m, key, iv):
    c=iv
    if len(m) % 16 != 0:
        return
    else:
        for i in range(0, len(m)/16):
            pc = set1.hex_xor.hex_xor(iv.encode('hex'), m[16*i:16*(i+1)].encode('hex')).decode('hex')
            iv = set1.AES_ECB.encrypt(pc, key)
            c = c+iv
        return c
```
最终结果
```python
if __name__ == '__main__':
    f = open('10.txt', 'r')
    c = set1.HexBase64.base642hex(f.read()).decode('hex')
    key = 'YELLOW SUBMARINE'
    iv = chr(0)*16
    print decrypt(c, key, iv)

ICE ICE BABY    
```

### 0x03 What's the point 
也没啥好说的 手动微笑 以后简单的直接传代码如何？
