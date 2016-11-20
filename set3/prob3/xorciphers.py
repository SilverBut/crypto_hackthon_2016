__author__ = 'Administrator'

def xorcrypt(m,k):
    return ''.join([chr(int(m[i],16)^int(k[i%len(k)],16)).encode('hex')[1] for i in range(0,len(m))])

def char2hex(ch):
    return ''.join([ch[i].encode('hex') for i in range(0,len(ch))])

if __name__=='__main__':
    m='''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
    k = 'ICE'
    print xorcrypt(char2hex(m),char2hex(k))