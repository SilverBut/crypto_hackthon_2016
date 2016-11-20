## Problem 19<problem id>. Break fixed-nonce CTR mode using substitutions

### 0x01 Question
利用之前的的CTR加密/解密功能，设其现时标志值为0，生成一个随机的AES密钥。
在连续加密(但不是一串流密码),加密的每一行以下的base64解码，产生40个独立密文。。
因为CTR不是随机的，每段密文会被相同的密钥流加密。实际的“加密”的一个字节的数据可以归结为一个异或操作,并且有这个规律：
```
CIPHERTEXT-BYTE XOR PLAINTEXT-BYTE = KEYSTREAM-BYTE
```
同时KEYSTREAM又都是相同的一段。
除此之外，还要通过字频来判断明文的正确性，这个代码set1写过，
### 0x02 Step

由于s要分段分块，所以Bxorciphers中的getlen需要改改
```python

def getthelen(c):
    loc = {}
    factors = []
    prolen = []
    for i in range(0, len(c)/2):
        if c[2*i:2*i+2] in loc:
            factors.append(i-loc[c[2*i:2*i+2]])
            loc[c[2*i:2*i+2]] = i
        else:
            loc[c[2*i:2*i+2]] = i
    for i in range(2, len(c)/2):
        cnt = 0
        for n in factors:
            if n % i != 0:
                continue
            else:
                cnt = cnt + 1
        if cnt >= len(factors)/10:
            prolen.append(i)
    min = 1
    for plen in prolen:
        fru = getfrupro(plen, c)
        if abs(fru-0.065) < min:
            min = abs(fru-0.065)
            thelen = plen
    return thelen
```
根据题干的提示，和pro6一样，寻找可能的KEY，并用字频攻击判断明文正确性，找到KEY后，
```python
s=getcpipher(c)
    print set1.Bxorciphers.xorciphers.xorcrypt(s[0],set1.Bxorciphers.getkey(s[0],set1.Bxorciphers.getthelen(s[0]))).decode('hex')
    print set1.Bxorciphers.getthelen(s[0])
   
```
最终锁定KEY
```python
 key1=set1.Bxorciphers.getkey(s[0],2)
    print key1
   
   KEY=0000 EXO ME?!
```
按位异或得正确答案，同pro5。好长一段 不贴了。。。
```
for t in c:
        print set1.Bxorciphers.xorciphers.xorcrypt(set1.HexBase64.base642hex(t),key1).decode('hex')
        
```

### 0x03 What's the point
