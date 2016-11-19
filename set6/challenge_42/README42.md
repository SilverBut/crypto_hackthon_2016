# Problem 42 rsa_e3_attack.py python2.7.6
库：hashlib

### 0x01 Question
要求实现e=3的rsa攻击
已知rsa的填充方式是先再头部加上0x0001，然后在消息尾部填充0xff，，然后再在后面加一个0x00，再加一个ASN1.hash,和前面消息的哈希，对这整个信息内容取3次方模n来得到签名，
然后再验证签名的正确性，验证签名的正确性就是验证哈希值等不等于hi mom
### 0x02 Step （main code）
由于验证填充的过程只是简单的对整个数字取三次方的模后，找到0x0001....0xff00，然后这个后面的字符串就当成哈希，所以我们可以构造信息0x0001ff00+hash
然后在后面填充0直到128个字节，然后接着我们需要找到某个数，这个数的三次方比我们构造的数大一点，但是前面直到哈希的部分都是相同的，也就是从小到大找到
某个数，这个数的3次方第一次大于了我们构造的数，然后这个数就是一个有效的签名了
关键代码就是产生这个三次方根的函数和构造字符串的过程：
m=fack_mes+'\xff'+'\x00'+hashmes+'\x00'*(128-len(fack_mes)-len(hashmes)-2)
#产生标签的函数
def creatSignature(m):
    t=1
    n=0
    for i in range(len(m)-1,-1,-1):
        n=n+ord(m[i])*t
        t=t*256
    #将字符串m转换成数字
    re=n/2
    tt=pow(re,3)
    l=0
    r=n
    while tt!=n:
        if tt>n:
            r=re
            re=(re+l)/2
        else:
            l=re
            re=(r+re)/2
        if l+1==r or l==r:
            re=re+1
            break
        tt=pow(re,3)
    #用二分法寻找这个三次方根
    return re

### 0x03 What's the point
填充的检测一定要完全检测，不能为了效率而认为对方一定按照这种方式填充，要考虑当前验证填充方式是否能构造出有效的能绕过检测的填充
重点：要找到最接近的三次方根

### 0x04 Reference
无

