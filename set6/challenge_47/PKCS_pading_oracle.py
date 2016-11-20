#coding:utf-8
import os
from gmpy2 import *

e = 65537

#检验前两位是不是0x0002，也就是判断其大小是不是在2B和3B减一之间
def check(c0, n, d):
    m=powmod(c0,d,n)
    if m>=2*B and m<3*B-1:
        return True
    else:
        return False


#对信息m进行填充的函数
def pad(m):
    padding_length = 29 - len(m)
    padding = '\x00'
    while '\x00' in padding:
        padding = os.urandom(padding_length)
    return '\x00'+'\x02'+padding+'\x00'+m

def char2int(m):
    t=0
    for i in range(0,len(m)):
        t*=256
        t+=ord(m[i])
    return t

def int2char(t):
    m=''
    i=32
    while t!=0:
        m=chr(t%256)+m
        t=t/256
        i=i-1
    m='\x00'*(32-len(m))+m
    return m

if __name__ == '__main__':
    n=83739148938054901060039023630603223785634357271762756404279802926818484254091
    d=4378809884656211696183129132887944942363852353690995145855455673603961676337
    msg = "kick it, CC"
    msg = pad(msg)
    print 'mes:',char2int(msg)
    c=powmod(char2int(msg),e,n)

    B = 2**(256-16)
    s1 = int(n/(3*B))
    M = [(2*B, 3*B-1)]
    #首先找到第一个s
    while True:
        ss1 = powmod(s1,e,n)
        c1 = c * ss1 % n
        f = check(c1, n, d)
        if f:
            break
        s1 += 1

    #然后执行第二步，缩小区间
    s = s1
    while M[0][1] != M[0][0]:
        flag = False
        a, b = M[0]
        #找到r和s使得能够通过检验
        r = int(2*((b*s - 2*B)/n))-1
        while not flag:
            r += 1
            for s in range((2*B + r*n)/b, (3*B + r*n)/a+1):
                encs = powmod(s,e,n)
                if check(c * encs % n, n, d):
                    flag = True
                    break
        #然后更新M
        if (2*B + r*n)% s==0:
            a1=(2*B + r*n)/ s
        else:
            a1=(2*B + r*n)/ s+1
        a = max([a, a1])
        b = min([b, (3*B -1 + r*n)/s])
        M = [(a, b)]
        if b - a < 1:
            print 'get:',b
            break



