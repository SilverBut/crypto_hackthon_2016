#coding:utf-8
__author__ = 'Administrator'

import hashlib
import random
p = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1

q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b


#g=p+1
g = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb2


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

#将字符串转换成相应的数字
def char2int(m):
    t=0
    for i in range(0,len(m)):
        t*=256
        t+=ord(m[i])
    return t

if __name__=="__main__":
    #z是随便取的
    z=random.randint(1,q)
    y=qpow(g,random.randint(0,q),p)
    #按照题意求得r和s
    r=qpow(g,z,p)%q
    z2,z1,z3=egcd(z,q)
    s=r*z1%q
    #对于任意的hm哈希值，这个标签都正确
    hm=char2int(hashlib.sha1("Hello, world").digest())
    if check(r,s,hm):
        print "yes,the signature is fine"
    hm=char2int(hashlib.sha1("Goodbye, world").digest())
    if check(r,s,hm):
        print "yes,the signature is fine"



