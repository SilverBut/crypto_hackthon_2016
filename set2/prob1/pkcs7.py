__author__ = 'Administrator'

def pkcs7(m,l):
    if len(m)%l!=0:
        return m+chr(l-len(m) % l)*(l-len(m) % l)
    else:
        return m+chr(l)*l


if __name__ == '__main__':
    m='YELLOW SUBMARINE'
    print pkcs7(m,20).encode('hex')
