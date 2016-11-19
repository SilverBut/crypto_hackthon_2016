# Problem 30. Break an MD4 keyed MAC using length extension

### 0x01 Question

与上一题差不多，只是对MD4的这种MAC进行攻击

### 0x02 Step (main code)

扩展后的明文的形式为 原明文+原padding+新明文

1. 首先模仿md4计算原文的摘要里的padding
2. 构造新的明文为old_message + old_pad + new_message
3. 模仿md4计算新的明文的padding
4. 这个新明文的哈希的结果我们是可以计算出来的,方法为下面的md4_hash_no_padding，但是与之前的题目不同，这次找的这个md4的类直接有接口进行下一轮迭代了，不用再写一个md4_hash_no_padding_

主要代码如下(python3.5)

```python
old_pad = gen_md4_padding(len(old_message) + i)

new_data = new_message
a = struct.unpack("<I", (old_tag[0:4]))[0]
b = struct.unpack("<I", (old_tag[4:8]))[0]
c = struct.unpack("<I", (old_tag[8:12]))[0]
d = struct.unpack("<I", (old_tag[12:16]))[0]
new_tag = MD4(A=a, B=b, C=c, D=d, numbytes=i+len(old_message +
                                                 old_pad)
             ).update(new_data).digest()
if check(old_message + old_pad + new_message, new_tag):
    print("congratz!")
    return new_tag
```
### 0x03 What's the point

原来python3.5和python2.7的编码方式有很多出入，= =

### 0x04 Reference

1. [github](https://github.com/josephw/python-md4/blob/master)
