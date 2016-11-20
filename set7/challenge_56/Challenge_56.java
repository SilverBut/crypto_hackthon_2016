import java.io.ByteArrayInputStream;
import java.util.Random;
import java.math.*;
public class Challenge_56 {

	private static final String cookie ="QkUgU1VSRSBUTyBEUklOSyBZT1VSIE9WQUxUSU5F";
	    public static String decry_RC4(byte[] data, String key) {  
	        if (data == null || key == null) {  
	            return null;  
	        }  
	        return asString(RC4Base(data, key));  
	    }  
	  
	    public static String decry_RC4(String data, String key) {  
	        if (data == null || key == null) {  
	            return null;  
	        }  
	        return new String(RC4Base(HexString2Bytes(data), key));  
	    }  
	  
	    public static byte[] encry_RC4_byte(String data, String key) {  
	        if (data == null || key == null) {  
	            return null;  
	        }  
	        byte b_data[] = data.getBytes();  
	        return RC4Base(b_data, key);  
	    }  
	  
	    public static String encry_RC4_string(String data, String key) {  
	        if (data == null || key == null) {  
	            return null;  
	        }  
	        return toHexString(asString(encry_RC4_byte(data, key)));  
	    }  
	  
	    private static String asString(byte[] buf) {  
	        StringBuffer strbuf = new StringBuffer(buf.length);  
	        for (int i = 0; i < buf.length; i++) {  
	            strbuf.append((char) buf[i]);  
	        }  
	        return strbuf.toString();  
	    }  
	  
	    private static byte[] initKey(String aKey) {  
	        byte[] b_key = aKey.getBytes();  
	        byte state[] = new byte[256];  
	  
	        for (int i = 0; i < 256; i++) {  
	            state[i] = (byte) i;  
	        }  
	        int index1 = 0;  
	        int index2 = 0;  
	        if (b_key == null || b_key.length == 0) {  
	            return null;  
	        }  
	        for (int i = 0; i < 256; i++) {  
	            index2 = ((b_key[index1] & 0xff) + (state[i] & 0xff) + index2) & 0xff;  
	            byte tmp = state[i];  
	            state[i] = state[index2];  
	            state[index2] = tmp;  
	            index1 = (index1 + 1) % b_key.length;  
	        }  
	        return state;  
	    }  
	  
	    private static String toHexString(String s) {  
	        String str = "";  
	        for (int i = 0; i < s.length(); i++) {  
	            int ch = (int) s.charAt(i);  
	            String s4 = Integer.toHexString(ch & 0xFF);  
	            if (s4.length() == 1) {  
	                s4 = '0' + s4;  
	            }  
	            str = str + s4;  
	        }  
	        return str;// 0x表示十六进制  
	    }  
	  
	    private static byte[] HexString2Bytes(String src) {  
	        int size = src.length();  
	        byte[] ret = new byte[size / 2];  
	        byte[] tmp = src.getBytes();  
	        for (int i = 0; i < size / 2; i++) {  
	            ret[i] = uniteBytes(tmp[i * 2], tmp[i * 2 + 1]);  
	        }  
	        return ret;  
	    }  
	  
	    private static byte uniteBytes(byte src0, byte src1) {  
	        char _b0 = (char) Byte.decode("0x" + new String(new byte[] { src0 })).byteValue();  
	        _b0 = (char) (_b0 << 4);  
	        char _b1 = (char) Byte.decode("0x" + new String(new byte[] { src1 })).byteValue();  
	        byte ret = (byte) (_b0 ^ _b1);  
	        return ret;  
	    }  
	  
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
	    
	    public static byte[] randomkey()
	    {
	    	Random r = new Random(System.currentTimeMillis()); 
	    	byte[] b = new byte[128];
	    	r.nextBytes(b);
	    	return b;
	    }
	    
	    public static byte[] Z16(byte[] cipher,int i) 
	    {
	    	//byte b;
	    	ByteArrayInputStream in = new ByteArrayInputStream(cipher); 
	    	int count = 0;
	    	while(count!=i-1){
	    		count+=in.skip(i-1-count);
	    	}
	    	byte[] btemp = new byte[1];
	    	in.read(btemp, 0, 1);
	    	//b = btemp[0];
	    	return btemp;
	    }
	    
	    
	    public static int[] getMax(int[] arr) {  
	        int max = Integer.MIN_VALUE; 
	        int location=0;
	        int[] r = new int[2];  
	        for(int i = 0; i < arr.length; i++) {  
	            if(arr[i] > max){  
	                max = arr[i];  
	                location=i;
	            }
	        }  
	        r[0]=max;
	        r[1]=location;
	        return r;  
	    }  
	    
	    /**
	     * int 转换成单位byte
	     * 可能会丢失精度
	     * 
	     * @param x 整数
	     * @return 一字节的byte
	     */
	    public static byte intToOnebyte(int x) {  
	        return (byte) x;  
	    }  
	    
	    /**
	     * 单字节byte 转换成int
	     * 
	     * @param byte b 一个单字节
	     * @return int
	     * 
	     */
	    public static int onebyteToInt(byte b) {  
	        //Java 总是把 byte 当做有符处理；我们可以通过将其和 0xFF 进行二进制与得到它的无符值  
	        return b & 0xFF;  
	    }  
	    
	    public static byte charToByte(char c)   
	    {  
	        return (byte) "0123456789ABCDEF".indexOf(c);  
	    } 
	  
	   
	    public static void main (String args[])
	    {
	    	
	    	System.out.println("W:"+charToByte('W')+"W:"+onebyteToInt(charToByte('W')));
	    	System.out.println("E:"+charToByte('E')+"E:"+onebyteToInt(charToByte('E')));
	    	//System.out.println("key:"+key.length());
	    	String plaintext =cookie;
	    	//String key = "password";
	    	
	    	//System.out.println("c byte:"+c);
	    	//System.out.println("c string:"+asString(c));
	    	
	    	//System.out.println("z16:"+asString(z16));
	    	//System.out.println("z16:"+onebyteToInt(z16[0]));
	    	int[] result = new int[256];
	    	int[] password = new int[256];  
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
	    	//String d=Challenge_56.decry_RC4(c, key);
	    	//System.out.println(d);
	    }
}



