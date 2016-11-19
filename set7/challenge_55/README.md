# Problem 55

### 0x01 Question
Challenge 55根据王小云的论文重新再现MD4算法的碰撞。

MD4是128位的哈希函数，王小云的论文主要指出的是，对于M可以找到一个姊妹原文M'，仅仅有几个字节差别而使得H（M）相等。
### 0x02 Step （main code）
```
#define IV0	0x67452301
#define IV1	0xefcdab89
#define IV2	0x98badcfe
#define IV3	0x10325476

#define RL(x, y) (((x) << (y)) | ((x) >> (32 - (y))))
#define RR(x, y) (((x) >> (y)) | ((x) << (32 - (y))))

#define F(b, c, d) (((c ^ d) & b) ^ d)
#define G(b, c, d) ((b & c) | (b & d) | (c & d))
#define H(b, c, d) (b ^ c ^ d)

#define K1	0x5A827999
#define K2	0x6ED9EBA1

unsigned int IV[4] = { IV0, IV1, IV2, IV3 };

unsigned int Q0[49], Q1[49];
unsigned int X0[16], X1[16];
```
首先初始化MD4的相关参数

### 0x03 What's the point
代码在Linux 上运行。
整个题目的内容其实就是重新再现MD4算法第一轮的时候第2到25步与第36到41步发生的差分碰撞。
花费半个小时去读读那篇王小云的论文之中 的东西再找找当时如何implement的source code

### 0x04 Reference
[1]Wang Xiaoyun's Paper http://www.infosec.sdu.edu.cn/uploadfile/papers/Cryptanalysis%20of%20the%20Hash%20Functions%20MD4%20and%20RIPEMD.pdf
[2]http://www.securiteam.com/tools/6O00E1FEKO.html
[3]Source Code http://www.securiteam.com/tools/6O00E1FEKO.html