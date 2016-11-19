__author__ = 'Administrator'

def detectECB(c):
    if len(c)%32!=0:
        return
    cs={}
    for i in range(0,len(c)/32):
        if c[i*32:(i+1)*32] in cs:
            return True
        else:
            cs[c[i*32:(i+1)*32]]=i
    return False

if __name__ == '__main__':
    f=open('8.txt','r')
    allc=f.readlines()
    for c in allc:
        if detectECB(c.strip('\n')):
            print 'yes'
            print c
            break

