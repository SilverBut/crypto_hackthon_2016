# Problem 1 PKCS_pading_oracle.py python 2.7.6
import os,gmpy2

### 0x01 Question
用选择密文攻击，构造一个oralce攻击，恢复m，其算法描述在论文中给出，但是可以不处理step2.b，也就是不处理多的情况

### 0x02 Step （main code）
第一步，构造第一个s，使得满足检验：
    #首先找到第一个s
    while True:
        ss1 = powmod(s1,e,n)
        c1 = c * ss1 % n
        oracle_check = check(c1, n, d)
        if oracle_check:
            break
        s1 += 1
然后根据论文中的描述：
在ri大于2*(b*si-2*B)/n的情况和si在(2*B + r*n)/b, (3*B + r*n)/a之间找到满足check的情况
        r = int(2*((b*s - 2*B)/n))-1
        while not flag:
            r += 1
            for s in range((2*B + r*n)/b, (3*B + r*n)/a+1):
                encs = powmod(s,e,n)
                if check(c * encs % n, n, d):
                    flag = True
                    break
根据找到的si更新区间M，使其为（max([a, (2*B + r*n)/s])，min([b, (3*B -1 + r*n)/s])）,其中，前面一个是向上取整，后面一个时向下取整
        if (2*B + r*n)% s==0:
            a1=(2*B + r*n)/ s
        else:
            a1=(2*B + r*n)/ s+1
        a = max([a, a1])
        b = min([b, (3*B -1 + r*n)/s])
        M = [(a, b)]
当M内的a,b相等时就为原始信息m

### 0x03 What's the point
即使是rsa也有oracle攻击，它是选择密文攻击
坑：这个算法感觉是概率性的，不一定能找到信息m。

### 0x04 Reference
Chosen Ciphertext Attacks Against Protocols
Based on the RSA Encryption Standard
PKCS #1

