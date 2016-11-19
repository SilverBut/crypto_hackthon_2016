# Problem 41 im_unpad_mr_oracle.py

### 0x01 Question
实现没有经过填充的rsa的攻击。
假设有信息p的密文c，我们得到了这个密文c，我们可以获得其他与c不同的密文的c1的解密结果p1，要求据此实现一个攻击，还原p
### 0x02 Step （main code）
首先我们随机产生一个s，求出(（s^e)mod n)*c)mod n，然后将得到的结果c1传给服务器，得到解密后的结果p1，然后根据p=（p1*s^-1)mod n获得原文p
因此关键代码就是：
#题目中的rsa的oracle过程，为s的e次方模n乘以c后再模n的结果
def rsa_oracle(s,e,n,c):
    return qpow(qpow(s,e,n)*c,1,n)

#获得原文p，对s取逆后乘以p1模n
def getP(p1,s,n):
    gcd,y,x=egcd(s,n)
    return qpow(p1*y,1,n)
两个函数。其中qpow函数时加了mod的快速幂，egcd是扩展欧几里得算法，输出中的y是逆

### 0x03 What's the point
没有经过任何修饰的rsa容易受到选择密文攻击

### 0x04 Reference
无

