__author__ = 'Administrator'

charfru={'e':12.25, 't':9.41,'a':8.19,'o':7.26,'i': 7.10,'n': 7.06,'r':6.85,'s':6.36,'h': 4.57,'d':3.91,'c':3.8312,'l':3.77,
'm': 3.34, 'p':2.89,'u' :2.58,'f': 2.2617, 'g': 1.71 ,'w': 1.59,'y': 1.58 ,'b': 1.47,'k': 0.4122, 'j': 0.14,'v':1.09,
'x': 0.2125, 'q': 0.09,'z': 0.08,' ':13}


def fru(cha):
    f=0
    for i in range(0,len(cha)):
        if cha[i].lower() in charfru:
            f+=charfru[cha[i].lower()]

    return f/(len(cha)*100)

def getchars(hex):
    max=0
    s=''
    for i in range(0,256):
        newch=''.join([chr(int(hex[2*j:2*j+2],16)^i) for j in range(0, len(hex)/2)])
        f=fru(newch)
        if f>max:
            max=f
            s=newch
            key=chr(i).encode('hex')
    return key,s

if __name__ == '__main__':
    hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print getchars(hex)
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