# Problem 57. Diffie-Hellman Revisited: Subgroup-Confinement Attacks

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


