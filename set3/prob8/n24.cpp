#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define cm 624//����ȷ�������Ԫ�صĸ��� 
int mt[cm];
//�������ӷ��������г�ʼ����
void init_PRG(int seed){
	int i=0;
	mt[0]=seed;
	for(i=1;i<cm;i++){
		mt[i]= (1812433253*(mt[i-1]^(mt[i-1]>>30))+i)&0xffffffff;
		//Ϊ����mt[i]ȷʵ��32λ�ķ�Χ�С� 
	}
}
void gene_PRG(){ //����PRG 
	int i,y;
	for(i=0;i<cm;i++){
		y=(mt[i]&0x80000000)|(mt[(i+1)%624]&0x7fffffff);//���û����㣬�൱�ڶ�������ӡ�
		mt[i]=mt[(i+397)%624]^(y>>1);
		if((y%2)==0){
			mt[i]=mt[i]^2567483615;
		} 
	} 
	//�൱�ڰ����е�mt[i]�������˳�ʼ������ˣ�Ϊ��ȷ�����ǵ�ֵ����32λ��
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

//ctr�ļ��� ,ֱ��ʹ��������������14��A�൱��8λ��ֵ��������з���
//14��A,ʹ�õ���Կ�ĳ�����32λ��ֱ�ӽ��м򻯣���Ҫ��������ֵ�� 
int ctrenc(int key,char *plaintext,int len){
	int j,i,count=0;
	//��ʵ�Ѿ�֪���������Ƕ��٣�
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
	//ǰ������12λ����ʣ��ʣ�����λ�����ж���ֱ��ʹ��enc1��ģ��ʣ�µ���λ
	hexa='a';
	enc1=hexa<<8+hexa;
	enc=enc^enc1;
}

int main(){
	int seed=0x1234;//ѡȡһ��16λ��������Ϊ���� 
	init_PRG(seed);//���ѡȡһ������С������ΪPRG��seed 
	int key=ext_PRG(0);//���ɵ�key�ĳ�����32λ�� 
	//iv�ĳ��Ⱥ���Կ�ĳ�����ͬ,���ѡȡһ��iv
	char plaintext[]="AAAAAAAAAAAAAA";
	int enc,enc1;//enc�з��ؼ���֮���ֵ�� 
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
