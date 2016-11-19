# coding:utf-8
def hex_xor(hexstring1,hexstring2):
    return "".join([chr(int(x,16)^int(y,16)).encode('hex')[1] for (x,y) in zip(hexstring1,hexstring2)])
	##先按位拆分两串字符串，按位异或后，连接字符串按hex编码。
	##zip([seql, …])接受一系列可迭代对象作为参数，将对象中对应的元素打包成一个个tuple元组，然后返回由这些tuples组成的list。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。
	##这里zip函数能让两串字符按位顺序排列。
	
if __name__=='__main__':
    hexstring1='1c0111001f010100061a024b53535009181c'
    hexstring2='686974207468652062756c6c277320657965'
    #746865206b696420646f6e277420706c6179
    print hex_xor(hexstring1,hexstring2)