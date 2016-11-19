#coding:utf-8
__author__ = 'Administrator'
import hashlib

str='hi mom'

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

#验证签名的函数
def verifySig(t):
    t=pow(t,3)
    i=127
    m=''
    while t!=0:
        m=chr(t%256)+m
        t=t/256
        i=i-1
    m='\x00'*(128-len(m))+m
    #首先将这个数转化为字符串
    if m[0:2]!='\x00\x01':
        return False
    #判断前两个字节
    i=0
    while m[i]!='\xff' and m[i+1]!='\x00':
        i+=1
        continue
    #找到填充的末尾
    if m[i:i+16]!=hashlib.md5('\x00\x01').digest() and m[i+16:i+32]!=hashlib.md5(str).digest():
        return True
    else:
        return False

if __name__=='__main__':
    fack_mes='\x00\x01'
    #构造哈希
    hashmes=hashlib.md5(fack_mes).digest()+hashlib.md5(str).digest()
    m='\x00'+hashmes
    #构造字符串
    m=fack_mes+'\xff'+'\x00'+hashmes+'\x00'*(128-len(fack_mes)-len(hashmes)-2)
    t=creatSignature(m)
    if verifySig(t)==True:
        print 'yes,the signature is right'
