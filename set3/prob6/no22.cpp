#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<dos.h>
#include<conio.h>
 
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
//ʹ�� 
int main(){
	int i;
	int seed=rand()%960+40;//ֱ����seedȡһ������ֵ���ٶ�seed���б���i
	int index=0;
	printf("seed =%d\n",seed);
	init_PRG(seed);
	int prg=ext_PRG(index);
	//printf("%d\n",index);
	printf("%d\n",prg);
	for(i=40;i<1000;i++){
		init_PRG(i);
		if(ext_PRG(index)==prg){
			//printf("%d\n",ext_PRG(index));
			printf("%d",i);
			break;
		}
	}	
} 
//  
