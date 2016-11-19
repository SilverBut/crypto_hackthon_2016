# Problem 45 DSA_par_tam.py python2.7.6
库：hashlib，random

### 0x01 Question
假如客户端允许提供其中的参数，如可以选择g，那么攻击者可能诱骗受害者选择不当的g，假如g=p+1，那么攻击者可以构造一个标签r，s，这个r，s对于任意的消息都是有效的标签
要求据此构造Hello, world和Goodbye, world的标签
### 0x02 Step （main code）
根据题意，对于任意的z
r = ((y**z) % p) % q
      r
s =  --- % q
      z
可以轻易的构造出r和s，只要先根据g=p+1构造出y就可以接着构造出y了
check函数如下：
#验证标签的正确
def check(r,s,hm):
    t,w,tt=egcd(s,q)
    u1=hm*w%q
    u2=r*w%q
    v=qpow(g,u1,p)*qpow(y,u2,p)%q
    if v==r:
        return True
    else:
        return False
求r和s：
    #z是随便取的
    z=random.randint(1,q)
    y=qpow(g,random.randint(0,q),p)
    #按照题意求得r和s
    r=qpow(g,z,p)%q
    z2,z1,z3=egcd(z,q)
    s=r*z1%q


### 0x03 What's the point
DSA签名不应该由用户决定其中的关键参数，否则会产生一些攻击

### 0x04 Reference
http://zhiqiang.org/blog/it/das-and-ecdsa-rsa.html

