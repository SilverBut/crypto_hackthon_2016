## Problem 11<problem id>. An ECB/CBC detection oracle

### 0x01 Question
编写一个函数，用一个未知的密钥加密数据。也就是说一个随机数决定用ECB还是CBC加密，各有1/2概率。

### 0x02 Step (main code)
import之前的 
```
import random
import AES_CBC_H,pkcs7
import AES_ECB
```
随机生成符合条件的密钥
```python
def random_key(l):
    if l%2!=0:
        l-=1
    return ''.join([chr(random.randint(0,255)) for i in range(0,l)])

```
随机加密过程如下：
```
def random_padm(m):
    return random_key(random.randint(5,10))+m+random_key(random.randint(5,10))

def random_encrypto(m):
    key = random_key(16)
    m = pkcs7.pkcs7(random_padm(m), 16)
    #ECB
    if random.randint(1, 2) == 1:
        return set1.AES_ECB.encrypt(m, key),'ECB'
    #CBC
    else:
        iv = random_key(16)
        return AES_CBC_H.encrypt(m, key, iv),'CBC'
```

最终可得两种不一样生成结果 多试几次就会发现有不一样的 :)
```python
if __name__ == '__main__':
    m=random_encrypto('this is a random encrypto!')
    print len(m[0])
    print m[1]   
```

### 0x03 What's the point 
生成随机密钥原来可以这样。。
