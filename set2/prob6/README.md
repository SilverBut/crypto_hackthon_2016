## Problem 14. Byte-at-a-time ECB decryption (Harder)

### 0x01 Question
选择明文攻击

现在生成一串随机字节不过作为攻击者预先预先考虑这个字符串的每一个明文。
即
```
AES-128-ECB(random-prefix || attacker-controlled || target-bytes, random-key)
```
目的还是破解目标字符串
### 0x02 Step (main code)
还是先base64解码出那串奇葩的明文：
```
Rollin' in my 5.0
With my rag-top down so my hair can blow
The girlies on standby waving just to say hi
Did you stop? No, I just drove by
```
测试类型是否为ECB
```python
def gettype(us):
    size=getblocksize(us)
    if len(encrypt_withs('',us))==len(us)/size*size+size:
        return 'ECB'
    else:
        return 'CBC'
```
按题给方法拼接、解密
```python
        for j in range(0, 256):
            c = encrypt_withs(ys+chr(j)+pad, us)
            if c[0:size] == c[len(ys)+len(pad)+1+i-size:len(ys)+len(pad)+1+i]:
                m += chr(j)
                break
                
def encrypt_withs(ys,us):
    m=pkcs7.pkcs7(ys+us, 16)
    return AES_ECB.encrypt(m,key)
```
### 0x03 What's the point
*"STIMULUS"* and *"RESPONSE"*

有 *刺激* 必有 *反应*

pro14选择明文攻击很明显比pro12方便很多