import java.io.ByteArrayInputStream;
import java.security.SecureRandom;
import java.security.Security;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

public class Ch52 {
	private static final String ALGORITHM = "AES";
	public static final String CIPHER_ALGORITHM = "AES/ECB/PKCS7Padding";
	private static int CACHE_SIZE = 8;
	private static int count =0;
	public static byte[] temp =new byte[CACHE_SIZE];
	public static byte[] encrypt(byte[] block, byte[] password) {  
        try {             
        		Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
        		//BOUNCYCASTLE Crypto tools!!!
        		KeyGenerator kgen = KeyGenerator.getInstance(ALGORITHM);  
                kgen.init(128, new SecureRandom(password));    //password AES 128
                SecretKey secretKey = kgen.generateKey();  
                byte[] enCodeFormat = secretKey.getEncoded();  
                //System.out.println("key:"+enCodeFormat.length);
                SecretKeySpec key = new SecretKeySpec(enCodeFormat, ALGORITHM);  
                Cipher cipher = Cipher.getInstance(ALGORITHM);            // 创建密码器   
                byte[] byteContent = block;  
                cipher.init(Cipher.ENCRYPT_MODE, key);                    // 初始化   
                byte[] result = cipher.doFinal(byteContent);  
                return result;                                            // 加密   
        } catch (Exception e) {  
                e.printStackTrace();  
        } 
        return null;  
        }  

	
	/**
	 * padding the input content (plaintext)
	 */
	public static String padding(String content)
	{
		int len = content.length();
		if(len%8==0){
			
			String padded = content;
			return padded;
		}
		else{
			int l = 8-(len%8);
			String padded = content;
			String str = "0";
			for(int i = 0;i<l;i++){
				padded = padded.concat(str);
			}
			System.out.println(padded);
			return padded;
		}
		//System.out.println(arg0);
	}
	
	
	public static String hash(byte[] content, byte[] password)
	{
		ByteArrayInputStream in = new ByteArrayInputStream(content);
		byte[] block = new byte[CACHE_SIZE]; 
		int nRead = 0;
		in.read(block, 0, CACHE_SIZE);
		temp=Ch52.encrypt(block, password);
		while((nRead=in.read(block, 0, CACHE_SIZE))!=-1){
			temp = Ch52.encrypt(block, temp);
		}
		String Hash = Ch52.byteToHex(temp);
		return Hash;
	}
	
	public static String byteToHex(byte b[]) {  
        if (b == null) {  
            throw new IllegalArgumentException(  
                    "Argument b ( byte array ) is null! ");  
        }  
        String hs = "";  
        String stmp = "";  
        for (int n = 0; n < b.length; n++) {  
            stmp = Integer.toHexString(b[n] & 0xff);  
            if (stmp.length() == 1) {  
                hs = hs + "0" + stmp;  
            } else {  
                hs = hs + stmp;  
            }  
        }  
        return hs.toLowerCase();  
    }  
	
	public static byte[] longToBytes(long num)   
    {  
        byte[] bytes = new byte[8];  
        for (int i = 0; i < 8; i++)   
        {  
            bytes[i] = (byte) (0xff & (num >> (i * 8)));  
        }  
  
        return bytes;  
    } 
	
	public static long collision(String hash1,String hash2)
	{
		for(long num = 0;num<999999999;num++){
			byte[] x =Ch52.longToBytes(num) ;
			//System.out.println(num);
			if((Ch52.hash(x, "000000".getBytes())==hash1)){
				System.out.println(num);
				if((Ch52.hash(x, "000000".getBytes())==hash2))
					return num;
			}
		}
		return 0;
		
		/*byte[] collide = new byte[256];
		for(byte b:collide){
			
			System.out.println(count++);
			for(int i=0;i<16;i++){
				b=(byte)i;
				if((Ch52.hash(collide, "000000".getBytes())==hash1)){
					System.out.println(Ch52.byteToHex(collide));
					return Ch52.byteToHex(collide);
				}
			}
		}
		return "None Expected!!!";*/
		
	}
	
	
	public static void main (String args[])
	{
		String content = "123";	
		String password = "000000";
		String padded =Ch52.padding(content);
		System.out.println("padded:"+padded);
		long num = 12300000;
		String t = String.valueOf(num);
		System.out.println("slong:"+t);
		System.out.println("long:"+Ch52.byteToHex(t.getBytes()));
		System.out.println(padded.length());
		System.out.println(Ch52.byteToHex(padded.getBytes()));
		String hash1 = Ch52.hash(padded.getBytes(), password.getBytes());
		CACHE_SIZE=16;
		String hash2 = Ch52.hash(padded.getBytes(), password.getBytes());
		//System.out.println("padded:"+padded.getBytes().length);
		//System.out.println("password:"+password.getBytes().length);
		System.out.println("hash1:"+hash1);
		System.out.println("hash2:"+hash2);
		System.out.println(collision(hash1,hash2));
	}
}