# Problem e9. Break a SHA-1 keyed MAC using length extension

### 0x01 Question

哈希长度扩展攻击
已知明文和MAC的结果，不知道密钥

### 0x02 Step (main code)

扩展后的明文的形式为 原明文新明文

1. 首先模仿SHA1计算原文的摘要里的padding
2. 构造新的明文为old_message + old_pad + new_message
3. 模仿SHA1计算新的明文的padding
4. 这个新明文的哈希的结果和我们是可以计算出来的,方法为下面的gen_sha1_hash

主要代码如下(python2.7)
```python
old_pad = gen_md_padding(len(old_message) + i)
new_pad = gen_md_padding(len(old_message) + len(old_pad) + len(new_message)
                         + i)
new_data = new_message + new_pad
a = struct.unpack(">I", (old_tag[0:4]))[0]
b = struct.unpack(">I", (old_tag[4:8]))[0]
c = struct.unpack(">I", (old_tag[8:12]))[0]
d = struct.unpack(">I", (old_tag[12:16]))[0]
e = struct.unpack(">I", (old_tag[16:20]))[0]
new_tag = sha1_hash_no_padding(new_data, (a, b, c, d, e))
```
### 0x03 What's the point


### 0x04 Reference

1. [github](https://raw.githubusercontent.com/ajalt/python-sha1/master/sha1.py)
