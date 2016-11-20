# Problem 56

### 0x01 Question
RC4密码的单字节偏移攻击。
### 0x02 Step （main code）
即RC4密码的某些字节位置上的密文出现的概率大于1/256.
```java
private static byte[] RC4Base(byte[] input, String mKkey) {  
	        int x = 0;  
	        int y = 0;  
	        byte key[] = initKey(mKkey);  
	        int xorIndex;  
	        byte[] result = new byte[input.length];  
	  
	        for (int i = 0; i < input.length; i++) {  
	            x = (x + 1) & 0xff;  
	            y = ((key[x] & 0xff) + y) & 0xff;  
	            byte tmp = key[x];  
	            key[x] = key[y];  
	            key[y] = tmp;  
	            xorIndex = ((key[x] & 0xff) + (key[y] & 0xff)) & 0xff;  
	            result[i] = (byte) (input[i] ^ key[xorIndex]);  
	        }  
	        return result;  
	    }  
```
RC4类
```java
public static byte[] randomkey()
	    {
	    	Random r = new Random(System.currentTimeMillis()); 
	    	byte[] b = new byte[128];
	    	r.nextBytes(b);
	    	return b;
	    }
	    
```
按要求随机生成128位的密钥进行加密。
```java
for(int i = 0;i<Math.pow(2,26);i++ ){
	    		System.out.println(i);
	    		byte[] rkey = randomkey();
	    		String key = asString(rkey);
	    		int k16 = onebyteToInt(Z16(rkey,16)[0]);
	    		password[k16]++;
	    		byte[] c = encry_RC4_byte(plaintext, key);
	    		byte[] z16 = Z16(c,16);
	    		int index =  onebyteToInt(z16[0]);
	    		result[index]++;
	    		
	    	}
	    	double[] resultn = new double[256];
	    	for(int i=0;i<256;i++){
	    		resultn[i]=(double)result[i]/Math.pow(2, 26);
	    	}
	    	
	    	
	    	
	    	
	    	int[] f = new int[256]; 
	    	for(int i=0;i<256;i++){
	    		for(int j=0;j<256;j++){
	    			int temp = i^j;
	    			f[i]+=password[j]*(Math.log(resultn[temp]));
	    		}
	    	}
	    	long maxvalue = getMax(f)[0];
	    	int location = getMax(f)[1];
	    	System.out.println("The 16th byte's value is the folloing max location:");
	    	System.out.println("maxvalue:"+maxvalue);
	    	System.out.println("max location:"+location);
```
按照Refernce之中的论文利用排列组合与多项分布公式去破解固定位置上原文。
### 0x03 What's the point
论文之中体现了前256位之中会发生RC4的单字节偏移。
这里没有完整破解cookie，可以利用控制位去实现。

这里以第16个字节内容进行了demo演示。
### 0x04 Reference
[1]All Your Biases Belong To Us: Breaking RC4 in WPA https://www.rc4nomore.com/vanhoef-usenix2015.pdf
[2]On the Security of RC4 in TLS and WPA https://cr.yp.to/streamciphers/rc4biases-20130708.pdf
