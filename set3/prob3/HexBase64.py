# coding: utf-8
import base64

def hex2base64(hexstring):
    return base64.b64encode(hexstring.decode('hex'))
# hex转base64：先解码hex再用base64编码
 

def base642hex(base64s):
    return base64.b64decode(base64s).encode('hex')
# base64转hex：先解码b64再编码成hex
##此外，字符串在Python内部的表示是unicode编码。所以本题中在做编码转换时，通常需要以unicode作为中间编码，即先将其他编码的字符串解码成unicode，再从unicode编码成另一种编码。 


if __name__=='__main__':
    hexstring='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print hex2base64(hexstring)
    base = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    print base642hex(base)


#####Base64编码广泛应用于MIME协议，作为电子邮件的传输编码，生成的编码可逆，后一两位可能有“=”，生成的编码都是ascii字符。

##### 优点：速度快，ascii字符，肉眼不可理解
##### 缺点：编码比较长，非常容易被破解，仅适用于加密非关键信息的场合