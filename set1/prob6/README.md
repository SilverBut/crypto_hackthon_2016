# Problem 6<id>. Break repeating-key XOR

### 0x01 Question
解密一段被repeating-key XOR 加密后的base64

### 0x02 Step （main code）、
此题可以直接暴力破解，也可以先锁定KEY，后者步骤如下：
-  尝试KEYSIZE的值从2到40。
-  写一个函数来计算两个字符串之间的编辑距离/汉明距离。
```python
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
``` 
- 为每个KEYSIZE，生成第一个KEYSIZE值生成的字节数和第二个KEYSIZE值生成的字节，并找到它们之间的编辑距离。
- 当KEYSIZE的距离最小时的KEY可能是真正的KEY，不过可能会得到KEYSIZE值生成最小的2~3个的，或者4个KEYSIZE块而不是2个和平均距离。

```python
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
```

- 用现在知道的可能的KEYSIZE:将密文分成KEYSIZE长度生成的密文成块。
- 现在转置块:一块是第一个字节的每一块,一块是第二个字节的每个块。。。
- 用pro4中的代码解决单个字符的异或。
- 对于每个块，单字节的异或KEY生成repeating-key异或的字节块。把它们拼接在一起就得到了KEY。
 
```python

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

 ```
最后暴力破解和锁定key破解得出相同答案
```python
if __name__ == '__main__':
    f = open('6.txt', 'r')
    s = HexBase64.base642hex(f.read())
    print decipher(s)
    #暴力破解
    print "**********************************************"
    print xorciphers.xorcrypt(s, getkey(s,getthelen(s))).decode('hex')
```


```
I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell 
In ecstasy in the back of me 
Well that's my DJ Deshay cuttin' all them Z's 
Hittin' hard and the girlies goin' crazy 
Vanilla's on the mike, man I'm not lazy. 

I'm lettin' my drug kick in 
It controls my mouth and I begin 
To just let it flow, let my concepts go 
My posse's to the side yellin', Go Vanilla Go! 

Smooth 'cause that's the way I will be 
And if you don't give a damn, then 
Why you starin' at me 
So get off 'cause I control the stage 
There's no dissin' allowed 
I'm in my own phase 
The girlies sa y they love me and that is ok 
And I can dance better than any kid n' play 

Stage 2 -- Yea the one ya' wanna listen to 
It's off my head so let the beat play through 
So I can funk it up and make it sound good 
1-2-3 Yo -- Knock on some wood 
For good luck, I like my rhymes atrocious 
Supercalafragilisticexpialidocious 
I'm an effect and that you can bet 
I can take a fly girl and make her wet. 

I'm like Samson -- Samson to Delilah 
There's no denyin', You can try to hang 
But you'll keep tryin' to get my style 
Over and over, practice makes perfect 
But not if you're a loafer. 

You'll get nowhere, no place, no time, no girls 
Soon -- Oh my God, homebody, you probably eat 
Spaghetti with a spoon! Come on and say it! 

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino 
Intoxicating so you stagger like a wino 
So punks stop trying and girl stop cryin' 
Vanilla Ice is sellin' and you people are buyin' 
'Cause why the freaks are jockin' like Crazy Glue 
Movin' and groovin' trying to sing along 
All through the ghetto groovin' this here song 
Now you're amazed by the VIP posse. 

Steppin' so hard like a German Nazi 
Startled by the bases hittin' ground 
There's no trippin' on mine, I'm just gettin' down 
Sparkamatic, I'm hangin' tight like a fanatic 
You trapped me once and I thought that 
You might have it 
So step down and lend me your ear 
'89 in my time! You, '90 is my year. 

You're weakenin' fast, YO! and I can tell it 
Your body's gettin' hot, so, so I can smell it 
So don't be mad and don't be sad 
'Cause the lyrics belong to ICE, You can call me Dad 
You're pitchin' a fit, so step back and endure 
Let the witch doctor, Ice, do the dance to cure 
So come up close and don't be square 
You wanna battle me -- Anytime, anywhere 

You thought that I was weak, Boy, you're dead wrong 
So come on, everybody and sing this song 

Say -- Play that funky music Say, go white boy, go white boy go 
play that funky music Go white boy, go white boy, go 
Lay down and boogie and play that funky music till you die. 

Play that funky music Come on, Come on, let me hear 
Play that funky music white boy you say it, say it 
Play that funky music A little louder now 
Play that funky music, white boy Come on, Come on, Come on 
Play that funky music 

**********************************************
I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell 
In ecstasy in the back of me 
Well that's my DJ Deshay cuttin' all them Z's 
Hittin' hard and the girlies goin' crazy 
Vanilla's on the mike, man I'm not lazy. 

I'm lettin' my drug kick in 
It controls my mouth and I begin 
To just let it flow, let my concepts go 
My posse's to the side yellin', Go Vanilla Go! 

Smooth 'cause that's the way I will be 
And if you don't give a damn, then 
Why you starin' at me 
So get off 'cause I control the stage 
There's no dissin' allowed 
I'm in my own phase 
The girlies sa y they love me and that is ok 
And I can dance better than any kid n' play 

Stage 2 -- Yea the one ya' wanna listen to 
It's off my head so let the beat play through 
So I can funk it up and make it sound good 
1-2-3 Yo -- Knock on some wood 
For good luck, I like my rhymes atrocious 
Supercalafragilisticexpialidocious 
I'm an effect and that you can bet 
I can take a fly girl and make her wet. 

I'm like Samson -- Samson to Delilah 
There's no denyin', You can try to hang 
But you'll keep tryin' to get my style 
Over and over, practice makes perfect 
But not if you're a loafer. 

You'll get nowhere, no place, no time, no girls 
Soon -- Oh my God, homebody, you probably eat 
Spaghetti with a spoon! Come on and say it! 

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino 
Intoxicating so you stagger like a wino 
So punks stop trying and girl stop cryin' 
Vanilla Ice is sellin' and you people are buyin' 
'Cause why the freaks are jockin' like Crazy Glue 
Movin' and groovin' trying to sing along 
All through the ghetto groovin' this here song 
Now you're amazed by the VIP posse. 

Steppin' so hard like a German Nazi 
Startled by the bases hittin' ground 
There's no trippin' on mine, I'm just gettin' down 
Sparkamatic, I'm hangin' tight like a fanatic 
You trapped me once and I thought that 
You might have it 
So step down and lend me your ear 
'89 in my time! You, '90 is my year. 

You're weakenin' fast, YO! and I can tell it 
Your body's gettin' hot, so, so I can smell it 
So don't be mad and don't be sad 
'Cause the lyrics belong to ICE, You can call me Dad 
You're pitchin' a fit, so step back and endure 
Let the witch doctor, Ice, do the dance to cure 
So come up close and don't be square 
You wanna battle me -- Anytime, anywhere 

You thought that I was weak, Boy, you're dead wrong 
So come on, everybody and sing this song 

Say -- Play that funky music Say, go white boy, go white boy go 
play that funky music Go white boy, go white boy, go 
Lay down and boogie and play that funky music till you die. 

Play that funky music Come on, Come on, let me hear 
Play that funky music white boy you say it, say it 
Play that funky music A little louder now 
Play that funky music, white boy Come on, Come on, Come on 
Play that funky music 
```