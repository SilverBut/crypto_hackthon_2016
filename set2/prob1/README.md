## Problem 9<problem id>.Implement PKCS#7 padding

### 0x01
将"YELLOW SUBMARINE"用PKCS#7填充至20字节

### 0x02 Step (main code)
差n位 就用n个n填充。
```
def pkcs7(m,l):
    if len(m)%l!=0:
        return m+chr(l-len(m) % l)*(l-len(m) % l)
    else:
        return m+chr(l)*l
```
检验如下，通过十六进制可看出末尾用04040404填充：
```
if __name__ == '__main__':
    m='YELLOW SUBMARINE'
    print pkcs7(m,20).encode('hex')
    
59454c4c4f57205355424d4152494e4504040404    
```

