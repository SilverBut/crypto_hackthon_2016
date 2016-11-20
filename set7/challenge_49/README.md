# Problem 1

### 0x01 Question
有个银行

用户发送消息的格式message || IV || MAC

IV随机生成
message的格式 

from=TOM&to=jinlaoban&amount=#1000000

### 0x02 Step （main code）

CBC 模式

S1= m[:16]异或IV异或

S2=S1异或m[16：32]

....


在CBC模式下 我们只要第一部分相等就可以了


所以我们 控制
IV' =m[:16]异或IV异或m'[:16]


S'=m'[:16]异或IV'=m'异或m[:16]异或IV异或m'[:16]=S


S=S'

攻击成功




### 0x03 What's the point
。。。讨论与结论。。坑在哪儿。。重点在哪儿。。。

### 0x04 Reference
[1]https://blog.cryptographyengineering.com/2013/02/15/why-i-hate-cbc-mac/