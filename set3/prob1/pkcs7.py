__author__ = 'Administrator'

def pkcs7(m,l):
    if len(m)%l!=0:
        return m+chr(l-len(m) % l)*(l-len(m) % l)
    else:
        return m+chr(l)*l

def d_pkcs7(m,l):
    n=ord(m[-1])
    if n>l:
        raise PadError('error length!')
    for i in range(-1,-n-1,-1):
        if ord(m[i])!=n:
            raise PadError('error padding!')
    return m[0:len(m)-n]

class PadError(RuntimeError):
    def __init__(self,args):
        self.args=args

if __name__ == '__main__':
    m1="ICE ICE BABY\x04\x04\x04\x04"
    m2="ICE ICE BABY\x05\x05\x05\x05"
    m3="ICE ICE BABY\x01\x02\x03\x04"
    try:
        # print d_pkcs7(m2, 16)
        # print d_pkcs7(m3, 16)
        print d_pkcs7(m1,16)
    except Exception,e:
         print e.args