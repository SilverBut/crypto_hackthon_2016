# Problem 51. Compression Ratio Side-Channel Attacks

### 0x01 Question

已知sessionid的长度，一个compression oracle，以及部分的request的信息"Cookie:sessionid="，要求恢复出session id来

### 0x02 Step (main code)

发送messgage，"Cookie:sessionid="，逐一添加字符，如果是正确的，通过compression oracle后的结果会比其他的小

测试方法

```python
python solve.py
```

### 0x03 What's the point

### 0x04 Reference
1. [lean the main exploit step from here](http://security.stackexchange.com/questions/19911/crime-how-to-beat-the-beast-successor/19914#19914)
2. [learn little from this paper, for it is too long](https://www.iacr.org/cryptodb/archive/2002/FSE/3091/3091.pdf)
3. [first material I found](http://crypto.stackexchange.com/questions/38047/compression-ratio-side-channel)
