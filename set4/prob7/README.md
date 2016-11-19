# Problem 31. Implement and break HMAC-SHA1 with an artificial timing leak

### 0x01 Question

利用服务器对HMAC后的摘要进行匹配的时延来判断我们构造的MAC是否是正确的

### 0x02 Step (main code)

关键代码如下(python2.7)
```python
for i in xrange(0x100):
    if index == 19:
        mac = set_byte(mac, index, chr(i))
        timing = attack_request(text, mac)
        delta = timing - current_timing
        if delta < 0.02 and delta > -0.02:
            final_timing.append(i)
            continue
        elif i == 0xff:
            return final_timing
        else:
            continue
    mac = set_byte(mac, index, chr(i))
    timing = attack_request(text, mac)
    delta = timing - current_timing
    if delta < 0.02 and delta > -0.02:
        mac_tmp = set_byte(mac, index + 1, chr(i))
        if check(text, index+1, mac_tmp, current_timing):
            return chr(i)

测试方法(要跑很久，结果见flag文件)
```shell
python solve.py > flag 2> log
python solve.py
```
### 0x03 What's the point

### 0x04 Reference
