## Problem <problem id>.

### 0x01
将"YELLOW SUBMARINE"填充至20字节

A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext. But we almost never want to transform a single block; we encrypt irregularly-sized messages.

One way we account for irregularly-sized messages is by padding, creating a plaintext that is an even multiple of the blocksize. The most popular padding scheme is called PKCS#7.

So: pad any block to a specific block length, by appending the number of bytes of padding to the end of the block. For instance,

"YELLOW SUBMARINE"

padded to 20 bytes would be:

"YELLOW SUBMARINE\x04\x04\x04\x04"
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

