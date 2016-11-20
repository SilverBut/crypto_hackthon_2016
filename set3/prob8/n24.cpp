#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define cm 624//用来确定数组的元素的个数 
int mt[cm];
//利用种子发生器进行初始化。
void init_PRG(int seed){
	int i=0;
	mt[0]=seed;
	for(i=1;i<cm;i++){
		mt[i]= (1812433253*(mt[i-1]^(mt[i-1]>>30))+i)&0xffffffff;
		//为了让mt[i]确实在32位的范围中。 
	}
}
void gene_PRG(){ //生成PRG 
	int i,y;
	for(i=0;i<cm;i++){
		y=(mt[i]&0x80000000)|(mt[(i+1)%624]&0x7fffffff);//利用或运算，相当于对两个相加。
		mt[i]=mt[(i+397)%624]^(y>>1);
		if((y%2)==0){
			mt[i]=mt[i]^2567483615;
		} 
	} 
	//相当于把所有的mt[i]都进行了初始化，因此，为了确定他们的值都是32位的
	for(i=0;i<cm;i++){
		mt[i]=mt[i]&0xffffffff;
	} 
} 
int ext_PRG(int index){
	if(index==0){
		gene_PRG();
	}
	int y=mt[index];
	y=y^(y>>11);
	y=y^((y<<7)&0x9d2c5680);
	y=y^((y<<15)&0xefc60000);
	y=y^(y>>18);
	index=(index+1)%624;
	return y;
}

//ctr的加密 ,直接使用流密码进行异或。14个A相当于8位的值，将其进行分类
//14个A,使用的密钥的长度是32位。直接进行简化，不要计数器的值。 
int ctrenc(int key,char *plaintext,int len){
	int j,i,count=0;
	//其实已经知道了明文是多少，
	int hexa;
	int enc=0,enc1=0;
	for(j=0;j<3;j++){
	for(i=0;i<4;i++){
		hexa=plaintext[i]; 
		enc=enc<<8+hexa;
	}
	enc=enc^key^count;
	count++;	
	}
	//前面解决了12位，还剩下剩余的两位不好判定，直接使用enc1来模拟剩下的两位
	hexa='a';
	enc1=hexa<<8+hexa;
	enc=enc^enc1;
}

int main(){
	int seed=0x1234;//选取一个16位的数字作为种子 
	init_PRG(seed);//随机选取一个超级小的数作为PRG的seed 
	int key=ext_PRG(0);//生成的key的长度是32位。 
	//iv的长度和密钥的长度相同,随机选取一个iv
	char plaintext[]="AAAAAAAAAAAAAA";
	int enc,enc1;//enc中返回加密之后的值。 
	int len=strlen(plaintext); 
	enc=ctrenc(key,plaintext,len);
	int seed1=0,key1;
	for(seed1=0;seed1<=0xffff;seed1++){
		init_PRG(seed1);
		key1=ext_PRG(0);
		enc1=ctrenc(key1,plaintext,len);
		if(enc1==enc){
			printf("successful");
			break;
		}
	}
} 
