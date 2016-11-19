## Problem 38.Offline dictionary attack on simplified SRP
	Offline dictionary attack on simplified SRP
  
### 0x01 Question
中间攻击获取SRP系统传输信息，从而本地爆破跑出password

### 0x02 Steps
模拟中间人生成 x, v,  A,  S 后本地爆破：
```
ass_list=[]
    with open("./dic.txt",'r') as f:
        for p in f.readlines():
            pass_list.append(p.strip('\n'))

    for pa in pass_list:
        x = hashlib.sha256(salt + bytes(pa, 'utf-8'))
        v = pow(g, int(x.hexdigest(), 16), N)
        A = pow(g, challenge33_iDH.a, N)
        S=pow(A * pow(v, u, N), challenge33_iDH.b, N)
        K = hashlib.sha256(str(S).encode()).hexdigest()
        temp=hashlib.pbkdf2_hmac('sha256', bytes(str(K), 'utf-8'), salt, 10000)
        if(temp==S2C):
            print(pa)
            break
```
### 0x03 the Point
中间人攻击；
计算S = (A * v**u) ** b % N的时候，可以考虑使用
```
pow(A * pow(v, u, N), b, N)
```
来做优化，否则pow()或者powmod()都会因计算量过大而卡死;
本地爆破字典要好。
### 0x04 Reference
