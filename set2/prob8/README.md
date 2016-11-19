## Problem 16<problem id>.CBC bitflipping attacks

### 0x01
已知明文攻击？？
随机产生一个AES密钥
结合填充代码和CBC代码编写两个函数。
第一个函数应该采取一个任意输入、预先构造的字符串:
```
"comment1=cooking%20MCs;userdata="
```
附加字符串
```
";comment2=%20like%20a%20pound%20of%20bacon"
```
- 函数应该引用”;“和“=”字符。
- 函数应该补齐16字节（AES块长度)，然后用随机AES加密。
- 第二个函数应该解密字符串和寻找字符";admin=true;"
- 返回true或false基于字符串是否存在。
- 如果第一个函数正确，应该不可能提供用户输入，将生成字符串寻找第二个函数。必须破解加密。
 
### 0x02 Step

随机AES加密
```python
def encrypto(s):
    return AES_CBC_H.encrypt(pkcs7.pkcs7(pre+s+last,16),key,iv)
```
替换明文关键步骤：
```python
def modifycipher(c):
    l=len(pre)
    m='%20MCs;userdata='.encode('hex')
    cm=';admin=true;aaaa'.encode('hex')
    cm=hex_xor.hex_xor(m,cm)
    return c[0:16]+set1.hex_xor.hex_xor(c[16:32].encode('hex'),cm).decode('hex')+c[32:]

```
### 0x03 What's the point
获取权限用'admin=true'替换'%20MCs;userdata='