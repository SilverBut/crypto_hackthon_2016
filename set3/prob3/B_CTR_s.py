__author__ = 'Administrator'
import AES_CTR
import HexBase64
import Bxorciphers

def getcpipher(cs):
    m=['','','']
    for c in cs:
        t=HexBase64.base642hex(c)
        #print t.decode('hex')
        m[0]+=t[0:32]
        if len(t)>=64:
            m[1]+=t[32:64]
            # print len(t)
    return m


if __name__ == '__main__':
    c=[
'SSBoYXZlIG1ldCB0aGVtIGF0IGNsb3NlIG9mIGRheQ==',
'Q29taW5nIHdpdGggdml2aWQgZmFjZXM=',
'RnJvbSBjb3VudGVyIG9yIGRlc2sgYW1vbmcgZ3JleQ==',
'RWlnaHRlZW50aC1jZW50dXJ5IGhvdXNlcy4=',
'SSBoYXZlIHBhc3NlZCB3aXRoIGEgbm9kIG9mIHRoZSBoZWFk',
'T3IgcG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==',
'T3IgaGF2ZSBsaW5nZXJlZCBhd2hpbGUgYW5kIHNhaWQ=',
'UG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==',
'QW5kIHRob3VnaHQgYmVmb3JlIEkgaGFkIGRvbmU=',
'T2YgYSBtb2NraW5nIHRhbGUgb3IgYSBnaWJl',
'VG8gcGxlYXNlIGEgY29tcGFuaW9u',
'QXJvdW5kIHRoZSBmaXJlIGF0IHRoZSBjbHViLA==',
'QmVpbmcgY2VydGFpbiB0aGF0IHRoZXkgYW5kIEk=',
'QnV0IGxpdmVkIHdoZXJlIG1vdGxleSBpcyB3b3JuOg==',
'QWxsIGNoYW5nZWQsIGNoYW5nZWQgdXR0ZXJseTo=',
'QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4=',
'VGhhdCB3b21hbidzIGRheXMgd2VyZSBzcGVudA==',
'SW4gaWdub3JhbnQgZ29vZCB3aWxsLA==',
'SGVyIG5pZ2h0cyBpbiBhcmd1bWVudA==',
'VW50aWwgaGVyIHZvaWNlIGdyZXcgc2hyaWxsLg==',
'V2hhdCB2b2ljZSBtb3JlIHN3ZWV0IHRoYW4gaGVycw==',
'V2hlbiB5b3VuZyBhbmQgYmVhdXRpZnVsLA==',
'U2hlIHJvZGUgdG8gaGFycmllcnM/',
'VGhpcyBtYW4gaGFkIGtlcHQgYSBzY2hvb2w=',
'QW5kIHJvZGUgb3VyIHdpbmdlZCBob3JzZS4=',
'VGhpcyBvdGhlciBoaXMgaGVscGVyIGFuZCBmcmllbmQ=',
'V2FzIGNvbWluZyBpbnRvIGhpcyBmb3JjZTs=',
'SGUgbWlnaHQgaGF2ZSB3b24gZmFtZSBpbiB0aGUgZW5kLA==',
'U28gc2Vuc2l0aXZlIGhpcyBuYXR1cmUgc2VlbWVkLA==',
'U28gZGFyaW5nIGFuZCBzd2VldCBoaXMgdGhvdWdodC4=',
'VGhpcyBvdGhlciBtYW4gSSBoYWQgZHJlYW1lZA==',
'QSBkcnVua2VuLCB2YWluLWdsb3Jpb3VzIGxvdXQu',
'SGUgaGFkIGRvbmUgbW9zdCBiaXR0ZXIgd3Jvbmc=',
'VG8gc29tZSB3aG8gYXJlIG5lYXIgbXkgaGVhcnQs',
'WWV0IEkgbnVtYmVyIGhpbSBpbiB0aGUgc29uZzs=',
'SGUsIHRvbywgaGFzIHJlc2lnbmVkIGhpcyBwYXJ0',
'SW4gdGhlIGNhc3VhbCBjb21lZHk7',
'SGUsIHRvbywgaGFzIGJlZW4gY2hhbmdlZCBpbiBoaXMgdHVybiw=',
'VHJhbnNmb3JtZWQgdXR0ZXJseTo=',
'QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4=']
    s=getcpipher(c)
    print len(c)
    print Bxorciphers.xorciphers.xorcrypt(s[0],Bxorciphers.getkey(s[0],Bxorciphers.getthelen(s[0]))).decode('hex')
    print Bxorciphers.getthelen(s[0])
    key1=Bxorciphers.getkey(s[0],2)
    print key1
    key2=Bxorciphers.getkey(s[1],32)
    for t in c:
        print Bxorciphers.xorciphers.xorcrypt(HexBase64.base642hex(t),key1).decode('hex')