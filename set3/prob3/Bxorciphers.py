__author__ = 'Administrator'
import HexBase64,xorciphers,xorcipherde

def getthelen(c):
    loc = {}
    factors = []
    prolen = []
    for i in range(0, len(c)/2):
        if c[2*i:2*i+2] in loc:
            factors.append(i-loc[c[2*i:2*i+2]])
            loc[c[2*i:2*i+2]] = i
        else:
            loc[c[2*i:2*i+2]] = i
    for i in range(2, len(c)/2):
        cnt = 0
        for n in factors:
            if n % i != 0:
                continue
            else:
                cnt = cnt + 1
        if cnt >= len(factors)/10:
            prolen.append(i)
    min = 1
    for plen in prolen:
        fru = getfrupro(plen, c)
        if abs(fru-0.065) < min:
            min = abs(fru-0.065)
            thelen = plen
    return thelen


def getfrupro(tlen, c):
    fru = [{} for n in range(0, tlen)]
    for i in range(0, len(c)/2):
        if c[2*i:2*i+2] in fru[i % tlen]:
            fru[i % tlen][c[2*i:2*i+2]] += 1
        else:
            fru[i % tlen][c[2*i:2*i+2]] = 1
    tsum = 0
    a = 0
    f=0
    for i in range(0, tlen):
        for v in fru[i]:
            a += fru[i][v]*fru[i][v]
            tsum += fru[i][v]
        f+=a*1.0/(tsum*tsum)
        a=0
        tsum=0
    return f/tlen


def getkey(c, tlen):
    #tlen = getThelen(c)
    tc = [[] for n in range(0,tlen)]
    mm = ' qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890\'\n.,;\t!`+-=()'
    for i in range(0, len(c)/2, 1):
        if c[2*i:2*i+2] not in tc[i % tlen]:
            tc[i % tlen].append(c[2*i:2*i+2])
    key = []
    for i in range(0, tlen):
        for ch in mm:
            mk = ord(ch) ^ ord(tc[i][0].decode('hex'))
            cnt = 1
            for k in range(1, len(tc[i])):
                if chr(mk ^ ord(tc[i][k].decode('hex'))) in mm:
                    cnt += 1
            if cnt == len(tc[i]):
                key.append(chr(mk).encode('hex'))
                break
    return ''.join(key)

def hammingdis(hex1, hex2):
    if len(hex1) != len(hex2):
        return
    hlen = 0
    for i in range(0,len(hex1)/2):
        n = int(hex1[2*i:2*i+2], 16) ^ int(hex2[2*i:2*i+2], 16)
        while n != 0:
            hlen += 1
            n = n & (n - 1)
    return hlen


def judgehammingdis(hex,tlen):
    s=[hex[2*tlen*i:2*tlen*(i+1)] for i in range(0,len(hex)/(2*tlen))]
    alen=0
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            alen+=hammingdis(s[i],s[j])/(tlen*1.0)
    alen/=(len(s)-1)*len(s)/2.0
    return alen

def getlen(hex):
    min = 100000
    plen = 0
    for i in range(1,50):
        l = judgehammingdis(hex, i)
        # print l,i
        if l < min:
            min = l
            plen = i
    return plen

def decipher(hex):
    tlen = getlen(hex)
    tm = [xorcipherde.getchars(''.join(hex[i:i+2] for i in range(2*j,len(hex),tlen*2)))[1] for j in range(0,tlen)]
    m=''
    for i in range(0,len(tm[0])):
        for j in range(0,tlen):
            if i>=len(tm[j]):
                break
            m=''.join([m, tm[j][i]])
    return m


if __name__ == '__main__':
    f = open('6.txt', 'r')
    s = HexBase64.base642hex(f.read())
    print decipher(s)
    print "**********************************************"
    print xorciphers.xorcrypt(s, getkey(s,getthelen(s))).decode('hex')