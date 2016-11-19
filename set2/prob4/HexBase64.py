import base64

def hex2base64(hexstring):
    return base64.b64encode(hexstring.decode('hex'))

def base642hex(base64s):
    return base64.b64decode(base64s).encode('hex')

if __name__=='__main__':
    hexstring='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print hex2base64(hexstring)
    base = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    print base642hex(base)