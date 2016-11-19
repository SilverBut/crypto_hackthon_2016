# Problem 50

### 0x01 Question
Challenge 50是针对两个JavaScript脚本的CBC MAC的碰撞，以此来表明CMAC并不适合去作为Hash。其实这个已经在Challenge 49之中已经有所体现，那就是CMAC对于变长消息并不具有安全性，攻击者可以控制IV从而实现改变消息m的内容而不改变。
这里根据已有的碰撞 JS脚本生成其CMAC（所谓的Hash）之后，对于另外一个给定的JS脚本加上注释符，仿照Challenge 49 的方法去构造。

理论知识，与原理分析在Challenge 49的README之中已经解释，实质还是扩展长度攻击
### 0x02 Step （main code）
Environment：Python 3

Library Needed：Crypto，Util；
### 0x03 What's the point
代码运行结果为构造的碰撞

//就是注释，所以之前的alert JS脚本肯定能运行
### 0x04 Reference


