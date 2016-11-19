# Problem 28. Implement a SHA-1 keyed MAC

### 0x01 Question

实现一个简单的MAC，SHA1(key || message)

### 0x02 Step (main code)

```python
def mac(key, data):
    return sha1(key + data)
```
### 0x03 What's the point


### 0x04 Reference

1. [github](https://raw.githubusercontent.com/ajalt/python-sha1/master/sha1.py)
