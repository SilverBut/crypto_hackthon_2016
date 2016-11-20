# Problem 48 challenge48.py python2.7.6
import rsa,gmpy2

### 0x01 Question
47题的升级版，扩大了密钥的长度，这个要用到论文中的step2.b，需要处理多个区间
### 0x02 Step （main code）
这题要求与上题相比，只差在了密钥长度上，因此需要用到第二部的b，这个需要处理多个区间的情况
对于多个区间的情况，需要递增s直到check通过：
        else:
            s1+=1
            while True:
                ss1 = powmod(s1,e,n)
                c1 = c * ss1 % n
                f = check(c1, n, d)
                if f:
                    break
                s1 += 1
            M=getM(M,s,B,n)
而对于M的处理，需要遍历a*s - 3*B + 1)/n,(b*s - 2*B)/n作为r，对每个a，b，求得所有的（max([a, (2*B + r*n)/s])，min([b, (3*B -1 + r*n)/s])）
的并集作为M返回：
#对多种情况进行处理
def getM(M,s,B,n):
    tM=[]
    for a,b in M:
        for r in range(int((a*s - 3*B + 1)/n),int((b*s - 2*B)/n)+1):
            if (2*B + r*n)% s==0:
                a1=(2*B + r*n)/ s
            else:
                a1=(2*B + r*n)/ s+1
            a1 = max([a, a1])
            b1 = min([b, (3*B -1 + r*n)/s])
            if a1<=b1 and a1>2*B and b1<3*B-1:
                tM.append((a1,b1))
    return tM
这样最后当M只有一个数据，而且a==b的时候就是m了

### 0x03 What's the point
rsa的oracle攻击对于长密钥仍有效，因此对于任何解密过程，千万不要泄露有关原文的任何信息
坑：与前一个相同，实际能否输出正确的m不一定

### 0x04 Reference
Chosen Ciphertext Attacks Against Protocols
Based on the RSA Encryption Standard
PKCS #1

