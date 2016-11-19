## Problem15 <problem id>.PKCS#7 padding validation

### 0x01
Write a function that takes a plaintext, determines if it has valid PKCS#7 padding, and strips the padding off.
编写一个函数，判断一个PKCS#7填充是否正确。

### 0x02 Step (main code)
PKCS#7填充差n位 就用n个n填充。判断逻辑很简单：
```
def d_pkcs7(m,l):
    n=ord(m[-1])
    if n>l:
        raise PadError('error length!')
    for i in range(-1,-n-1,-1):
        if ord(m[i])!=n:
            raise PadError('error padding!')
    return m[0:len(m)-n]

class PadError(RuntimeError):
    def __init__(self,args):
        self.args=args
```
检验如下，m1正确，m2、m3错误
```
if __name__ == '__main__':
    m1="ICE ICE BABY\x04\x04\x04\x04"
    m2="ICE ICE BABY\x05\x05\x05\x05"
    m3="ICE ICE BABY\x01\x02\x03\x04"
    try:
        print d_pkcs7(m1, 16)
        print d_pkcs7(m2, 16)
        print d_pkcs7(m3,16)
    except Exception,e:
         print e.args   
```


