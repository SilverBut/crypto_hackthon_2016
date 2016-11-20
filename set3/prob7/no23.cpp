#include<stdio.h>

#define cm 624//用来确定数组的元素的个数 
int mt[cm];
int index=0;
//利用种子发生器进行初始化。
void init_PRG(int seed){
	int i=0;
	mt[0]=seed;
	for(i=1;i<cm;i++){
		mt[i]= (1812433253*(mt[i-1]^(mt[i-1]>>30))+i)&0xffffffff;
		//为了让mt[i]确实在32位的范围中。 
	}
}
//对于同一个初始化的种子，mt[i]都是相同的值。 
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
	index=(index+1)%cm;//每次经过624位，要是index=0,那么：就重新生成一遍gene_PRG（）；因为这个时候已经改变了m[i]数组，所以肯定不会在624位产生一个相同的输出 
	return y;
}

int reverse(int x){
	 x^=(x>>18);     //第一步直接就是反解得到正常的值
	 	
	 int part1;	
	 x=(x<<15)&0xefc60000;   //不用对最高位判断，一定能得到结果。因为异或的置是6，所以2+4，直接处理左移15位就是正确的，得到了y<<15; 
	 
	 int part2;
	 part1=(x<<7)&0x3fff;     //使用一个part2对值进行判断。 确定x<<7位的前14位。剩下的值用位运算或者是暴力穷举解。
	 for(part1;part1<0xffffffff;part1=part1+1<<14){     //对剩下不能确定的11位进行穷举分析，要是直接在位运算中，穷举的次数会降低。 
	 	part2=(part1&0x9d2c5680)^x;//part2中存放真实的值 
	 	if((part2^((part2<<7)&0x9d2c5680))==x){
	 		x=part2;
		 }
	 }//执行过程中直接穷举的代价太大，穷举的次数超过了能承受的范围，得不到正确的取值，按照位运算进行分析，判断位中不正确的值。 
	 
	 //已知第21位到第31位的信息，缺少第11位到第20位的信息。穷举分析 
	  part1=(part1>>11)&0xfffff4ff;
	  int j;
	  for(j=0;j<0x3ff;j=j+0x1){
	  	part1=part1+j;//part1中存放的值是y>>11的值。
		part2=part1^x; 
	  	if(((part2>>11)^part2)==x){
	  		x=part2;
		  }
	  }//跑1024次 
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
		mt0[i]=ext_PRG();//在mt[0]中存放初始的值， 
	}
	for(i=0;i<cm;i++){
		mt1[i]= ext_PRG();
	}
	//现在的目标就是反转，先进行反转，再进行比较，其中不正确的值就直接输出错误。 
	for(i=0;i<cm;i++){
		mt1[i]=reverse(mt1[i]);
		compare(mt1[i],mt0[i]);
	}
} 
//这个算法中间肯定是移位的时候出了错误，怎么解决移位问题，反解一下，重新取值。 
