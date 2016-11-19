#include<stdio.h>

#define cm 624//用来确定数组的元素的个数 
int mt[cm];
int index;
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
int ext_PRG(){
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
int main(){
    int seed;
	printf("input a seed:");
	scanf("%d",&seed);
	init_PRG(seed);
	int i;
	for(i=0;i<10;i++){
		printf("%d\n",ext_PRG());
	}	
} 
