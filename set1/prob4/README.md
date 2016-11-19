# Problem 4<id>. Detect single-character XOR

### 0x01 Question

此题要求解密一串用一个字符异或后的十六进制编码的字符串，可以用pro3的代码解。

### 0x02 Step （main code）
首先查得所有英文字母的使用频率.
 ```python
charfru={'e':12.25, 't':9.41,'a':8.19,'o':7.26,'i': 7.10,'n': 7.06,'r':6.85,'s':6.36,'h': 4.57,'d':3.91,'c':3.8312,'l':3.77,
'm': 3.34, 'p':2.89,'u' :2.58,'f': 2.2617, 'g': 1.71 ,'w': 1.59,'y': 1.58 ,'b': 1.47,'k': 0.4122, 'j': 0.14,'v':1.09,
'x': 0.2125, 'q': 0.09,'z': 0.08,' ':13}
    
 ```
然后 在getchar函数中用* i {range(0,256)}* 与密文字符串按位异或，用* fru* 函数筛选可能正确的明文

```python
def fru(cha):
    f=0
    for i in range(0,len(cha)):
        if cha[i].lower() in charfru:
            f+=charfru[cha[i].lower()] 
            #将所有返回字符为小写字母的位与字母频率表比对
            #若在表中，频率相加
    return f/(len(cha)*100)

def getchars(hex):
    max=0
    s=''
    for i in range(0,256):
        newch=''.join([chr(int(hex[2*j:2*j+2],16)^i) for j in range(0, len(hex)/2)])   
        #按十六进制编码后与字符i异或，再按位拼接 
        f=fru(newch)  #最终返回每个i与字符串异或后的总字母频率值
        if f>max:
            max=f  
            s=newch   #选出总频率最大的，即为正确明文。
            key=chr(i).encode('hex')#key为字符i的hex编码
    return key,s
 ```
 即可得到正确答案，看上去还是像一句正常的话的 :）继续卖萌
 ```python
 if __name__ == '__main__':
    f=open('4.txt','r')
    cs=f.readlines()
    max=0
    rs=''
    for s in cs:
        ps=getchars(s)
        f=fru(ps[1])
        if f>max:
            max=f
            rs=ps
    print rs
    
('35', 'Now that the party is jumping\n')
 ```
### 0x03 What's the point
同pro3


### 0x04 Reference
同pro3
