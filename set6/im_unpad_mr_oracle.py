#coding:utf-8
__author__ = 'Administrator'
import random

#扩展欧几里得算法，输出y为逆
def egcd(a,b):
	if b==0:
		return a,1,0
	else:
		gcd,x,y=egcd(b,a%b)
		return gcd,y,x-a/b*y

#快速幂算法，附带模mod
def qpow(g,x,mod):
	r=1
	while x!=0:
		if x&1==1:
			r=(r*g)%mod
		g=(g*g)%mod
		x=x>>1
	return r

#题目中的rsa的oracle过程，为s的e次方模n乘以c后再模n的结果
def rsa_oracle(s,e,n,c):
    return qpow(qpow(s,e,n)*c,1,n)

#获得原文p，对s取逆后乘以p1模n
def getP(p1,s,n):
    gcd,y,x=egcd(s,n)
    return qpow(p1*y,1,n)


if __name__=="__main__":
    p=47
    q=59
    #大素数n
    n=p*q
    #公钥e
    e=63
    #私钥d
    d=847
    #假设信息为m
    m=500       #信息为m
    s=random.randint(0,p*q)         #随机的s
    c=qpow(m,e,n)
    c1=rsa_oracle(s,e,n,c)
    p1=qpow(c1,d,n)
    print getP(p1,s,n)              #通过随机的s得到p