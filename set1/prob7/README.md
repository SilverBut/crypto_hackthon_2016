# Problem 7<id>. AES in ECB mode

### 0x01 Question
解密*7.txt*中的base64编码的内容,这个文件已经用KEY=*"YELLOW SUBMARINE"*在AES-128的ECB模式下进行加密.
### 0x02 Step （main code）

 ```python

def decrypt(c,key):
    encryptor=Crypto.Cipher.AES.new(key,Crypto.Cipher.AES.MODE_ECB)
    return encryptor.decrypt(c)

def encrypt(m,key):
    encryptor=Crypto.Cipher.AES.new(key,Crypto.Cipher.AES.MODE_ECB)
    return encryptor.encrypt(m)
    
 ```
直接调用 Crypto.Cipher.AES库（安装教程见Reference）中的函数对AES-128的ECB模式进行加密解密。认证。

```python
if __name__ == '__main__':
    f=open('7.txt','r')
    c=set1.HexBase64.base642hex(f.read()).decode('hex')
    key='YELLOW SUBMARINE'
    print decrypt(c,key)
 ```
### 0x03 What's the point

Crypto.Cipher.AES库能解决所有问题，就是win版安装麻烦。。。推荐Linux版

### 0x04 Reference
https://dbaportal.eu/2011/11/10/how-to-compile-pycrypto-2-4-1-python-3-2-2-for-windows-7-x64/
http://www.voidspace.org.uk/python/modules.shtml#pycrypto