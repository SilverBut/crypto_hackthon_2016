## Problem 34.Imeplement a MITM key-fixing attack on Diffie-Hellman with parameter injection

### 0x01 Question
这题要求做一个DH的中间人攻击。

### 0x02 Environment
* Python3.5 with pycrypto

### 0x03 Steps
1. A发`p, g, A`给M，同时M将其中的__A__替换为__p__发给B。
2. B发`B`给M，同时M讲其中的__B__替换为__p__发给A。
3. A拥有密钥`(p ** a) % p`，B拥有秘钥`(p ** b) % p`，M拥有A与B的秘钥。
4. 当A发包给B时，首先经过M。在这里，M讲数据包用A的秘钥解包，再用B的秘钥打包并发给B。
5. 这就实现了中间人攻击，M可以查看所有的数据包，且A的包经过M的中继能够让B解开，反之亦然。


