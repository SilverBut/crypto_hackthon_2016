# Problem 26. CTR bitflipping

### 0x01 Question

通过修改AES-CTR加密的密文，来达到控制明文的目的

### 0x02 Step (main code)

第一次上传时只要把数据设置成 '\x00' * 0x10，即可获得key_stream，然后就可以控制明文了

```python
attacked_keystream = ct_cus_raw[(attacked) * 0x10: (attacked + 1) * 0x10]
target      = ";admin=true;AAAA"
attacked_fi = repeat_xor(attacked_keystream, target)
payload1    = (ct_cus_raw[:(attacked) * 0x10] +
               attacked_fi +
               ct_cus_raw[(attacked + 1) * 0x10:])
```
### 0x03 What's the point


### 0x04 Reference

1. [wiki](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#CBC)
