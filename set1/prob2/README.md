# Problem 2<id>. Fixed XOR<name>

### 0x01 Question
Write a function that takes two equal-length buffers and produces their XOR combination.

此题要求我们写一个函数可以得到两段等长字符串的异或值，并加以验证

### 0x02 Step （main code）

 ```python
def hex_xor(hexstring1,hexstring2):
    return "".join([chr(int(x,16)^int(y,16)).encode('hex')[1] for (x,y) in zip(hexstring1,hexstring2)])
    
 ```
 先按位拆分两串字符串，按位异或后，连接字符串按hex编码。

用题目所给字符串检验，给出正确答案。
```python
if __name__=='__main__':
    hexstring1='1c0111001f010100061a024b53535009181c'
    hexstring2='686974207468652062756c6c277320657965'
    #746865206b696420646f6e277420706c6179
    print hex_xor(hexstring1,hexstring2)

746865206b696420646f6e277420706c6179
 ```
### 0x03 What's the point
其中用到了的zip函数能让两串字符按位顺序排列。
 ```
 >>> help(zip)
Help on built-in function zip in module __builtin__:

zip(...)
    zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]
    
    Return a list of tuples, where each tuple contains the i-th element
    from each of the argument sequences.  The returned list is truncated
    in length to the length of the shortest argument sequence.
 ```
*zip([seql, ...])*接受一系列可迭代对象作为参数，将对象中对应的元素打包成一个个tuple元组，然后返回由这些tuples组成的list。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。


### 0x04 Reference
http://www.cnblogs.com/BeginMan/archive/2013/03/14/2959447.html
