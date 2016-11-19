# Problem 5<id>. Implement repeating-key XOR

### 0x01 Question
```
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
```
此题要求我们用密钥*ICE* 加密上一段话，使用repeating-key XOR。

repeating-key XOR，是指按顺序依次使用ICE的每个字节，一个字节的明文将会与*I*异或，下一个*C*，下一个*E*，然后再轮到*I* 等等。


### 0x02 Step （main code）
先按位编码再按位异或解密
 ```python
def xorcrypt(m,k):
    return ''.join([chr(int(m[i],16)^int(k[i%len(k)],16)).encode('hex')[1] for i in range(0,len(m))])

def char2hex(ch):
    return ''.join([ch[i].encode('hex') for i in range(0,len(ch))])

 ```
用题目所给字符串检验，给出正确答案。
```python
if __name__=='__main__':
    m='''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
    k = 'ICE'
    print xorcrypt(char2hex(m),char2hex(k))

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```

### 0x03 What's the point

### 0x04 Reference
