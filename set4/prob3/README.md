# Problem 27. Recover the key from CBC with IV=Key

### 0x01 Question

在CBC模式加密中，会有人用IV直接做key来进行加密，这样是不安全的，因为IV是可以恢复出来的

### 0x02 Step (main code)

```python
pt1_raw     = "A" * 0x10
pt2_raw     = "B" * 0x10
pt3_raw     = "C" * 0x10
payload0    = pt1_raw + pt2_raw + pt3_raw
ct_cus_raw  = do_enc(pre_raw, suf_raw, payload0)

# exploit
payload1    = (ct_cus_raw[:0x10] +
               "\x00"* 0x10 +
               ct_cus_raw[:0x10])

# receiver check result
res, recov  = do_dec_check(pre_raw, suf_raw, payload1)
```
### 0x03 What's the point


### 0x04 Reference

1. [wiki](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#CBC)
