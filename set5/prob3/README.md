## Problem 35.Implement DH with negotiated groups, and break with malicious "g" parameters

### 0x01 Question
这题要求使用`g`参数来进行中间人攻击。

### 0x02 Environment
* Python3.5 with pycrypto

### 0x03 Steps
* 当使用`g = 1`时，所计算出来的__A__与__B__都等于__0__。这就导致最终协商的秘钥为__0__。
* 当使用`g = p`时，所计算出来的__A__与__B__均为__1__，这就导致最终协商的密钥为__1__。
* 当使用`g = p - 1`时，所计算出来的__A__与__B__的值为`1 or p-1`，其中两个值交替出现，因此也很容易猜解得到最终密钥。

