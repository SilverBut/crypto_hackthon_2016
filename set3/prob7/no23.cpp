#include<stdio.h>

#define cm 624//����ȷ�������Ԫ�صĸ��� 
int mt[cm];
int index=0;
//�������ӷ��������г�ʼ����
void init_PRG(int seed){
	int i=0;
	mt[0]=seed;
	for(i=1;i<cm;i++){
		mt[i]= (1812433253*(mt[i-1]^(mt[i-1]>>30))+i)&0xffffffff;
		//Ϊ����mt[i]ȷʵ��32λ�ķ�Χ�С� 
	}
}
//����ͬһ����ʼ�������ӣ�mt[i]������ͬ��ֵ�� 
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
int ext_PRG(){
	if(index==0){
		gene_PRG();
	}
	int y=mt[index];
	y=y^(y>>11);
	y=y^((y<<7)&0x9d2c5680);
	y=y^((y<<15)&0xefc60000);
	y=y^(y>>18);
	index=(index+1)%cm;//ÿ�ξ���624λ��Ҫ��index=0,��ô������������һ��gene_PRG��������Ϊ���ʱ���Ѿ��ı���m[i]���飬���Կ϶�������624λ����һ����ͬ����� 
	return y;
}

int reverse(int x){
	 x^=(x>>18);     //��һ��ֱ�Ӿ��Ƿ���õ�������ֵ
	 	
	 int part1;	
	 x=(x<<15)&0xefc60000;   //���ö����λ�жϣ�һ���ܵõ��������Ϊ��������6������2+4��ֱ�Ӵ�������15λ������ȷ�ģ��õ���y<<15; 
	 
	 int part2;
	 part1=(x<<7)&0x3fff;     //ʹ��һ��part2��ֵ�����жϡ� ȷ��x<<7λ��ǰ14λ��ʣ�µ�ֵ��λ��������Ǳ�����ٽ⡣
	 for(part1;part1<0xffffffff;part1=part1+1<<14){     //��ʣ�²���ȷ����11λ������ٷ�����Ҫ��ֱ����λ�����У���ٵĴ����ή�͡� 
	 	part2=(part1&0x9d2c5680)^x;//part2�д����ʵ��ֵ 
	 	if((part2^((part2<<7)&0x9d2c5680))==x){
	 		x=part2;
		 }
	 }//ִ�й�����ֱ����ٵĴ���̫����ٵĴ����������ܳ��ܵķ�Χ���ò�����ȷ��ȡֵ������λ������з������ж�λ�в���ȷ��ֵ�� 
	 
	 //��֪��21λ����31λ����Ϣ��ȱ�ٵ�11λ����20λ����Ϣ����ٷ��� 
	  part1=(part1>>11)&0xfffff4ff;
	  int j;
	  for(j=0;j<0x3ff;j=j+0x1){
	  	part1=part1+j;//part1�д�ŵ�ֵ��y>>11��ֵ��
		part2=part1^x; 
	  	if(((part2>>11)^part2)==x){
	  		x=part2;
		  }
	  }//��1024�� 
	  return x;
}

void compare(int x,int y){
	if(x!=y){
		printf("error");
	}
}

int main(){
    int seed;
    int mt0[cm];
    int mt1[cm]; 
	printf("input a seed:");
	scanf("%d",&seed);
	init_PRG(seed);
	int i;
	for(i=0;i<cm;i++){ 
		mt0[i]=ext_PRG();//��mt[0]�д�ų�ʼ��ֵ�� 
	}
	for(i=0;i<cm;i++){
		mt1[i]= ext_PRG();
	}
	//���ڵ�Ŀ����Ƿ�ת���Ƚ��з�ת���ٽ��бȽϣ����в���ȷ��ֵ��ֱ��������� 
	for(i=0;i<cm;i++){
		mt1[i]=reverse(mt1[i]);
		compare(mt1[i],mt0[i]);
	}
} 
//����㷨�м�϶�����λ��ʱ����˴�����ô�����λ���⣬����һ�£�����ȡֵ�� 
