# Problem 8<id>.Detect AES in ECB mode

### 0x01 Question
解密*8.txt*中的base64编码的内容,在这个文件中是一群hex编码的密文。

其中一个用ECB加密，检测出它。
ECB问题在于,它是无状态的,确定的

相同的16字节明文密文块总是会产生相同的16个字节。
### 0x02 Step （main code）
cs里放入无重复的字节，一旦遇到相同的字符，找到ECB模式加密的，返回true
 ```python
def detectECB(c):
    if len(c)%32!=0:
        return
    cs={}
    for i in range(0,len(c)/32):
        if c[i*32:(i+1)*32] in cs:
            return True
        else:
            cs[c[i*32:(i+1)*32]]=i
    return False
    
 ```
答案：

```python
if __name__ == '__main__':
    f=open('8.txt','r')
    allc=f.readlines()
    for c in allc:
        if detectECB(c.strip('\n')):
            print 'yes'
            print c
            break
```
返回结果
```
yes
d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a
            
 ```
