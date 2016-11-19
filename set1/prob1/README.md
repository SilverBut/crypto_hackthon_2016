# Problem 1<id>. Convert hex to base64

### 0x01 Question
Write a function that takes two equal-length buffers and produces their XOR combination.

此题要求我们将十六进制转换为base64，以后的练习将经常用到此转换代码。

同时告诉我们一个*Cryptopals Rule*：
##### 密码学中通常使用原始字节而不是编码后字符串，十六进制和base64的用处只是更好看地显示。
### 0x02 Step （main code）

 ```python
def hex2base64(hexstring):
    return base64.b64encode(hexstring.decode('hex'))

def base642hex(base64s):
    return base64.b64decode(base64s).encode('hex')
    
 ```
 hex转base64：先解码hex再用base64编码
 
 base64转hex：先解码b64再编码成hex
 
 简单的编码应用，二者可自由转换。

用题目所给字符串检验，给出正确答案。
```python
if __name__=='__main__':
    hexstring='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print hex2base64(hexstring)

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
```
```
    base = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    print base642hex(base)
    
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
 ```
### 0x03 What's the point
Base64编码广泛应用于MIME协议，作为电子邮件的传输编码，生成的编码可逆，后一两位可能有“=”，生成的编码都是ascii字符。

##### 优点：速度快，ascii字符，肉眼不可理解
##### 缺点：编码比较长，非常容易被破解，仅适用于加密非关键信息的场合

此外，字符串在Python内部的表示是unicode编码。所以本题中在做编码转换时，通常需要以unicode作为中间编码，即先将其他编码的字符串解码成unicode，再从unicode编码成另一种编码。 


### 0x04 Reference
http://blog.csdn.net/lxdcyh/article/details/4021476