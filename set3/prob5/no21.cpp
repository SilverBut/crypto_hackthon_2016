/*在c语言中可以直接对整数进行异或，*/
/*梅森旋转素数的生成方法是对大整数进行异或*/ 
#include<stdio.h> /*Periodparameters*/
#define N 624
#define M 397 
#define MATRIX_A 0x9908b0dfUL 
#define UPPER_MASK 0x80000000UL/*most significant w-rbits*/
#define LOWER_MASK 0x7fffffffUL/*least significant rbits*/

static unsigned long mt[N];/*the  array  for   the  state  vector*/
static int mti=N+1;
void init_genrand(unsigned long s)
{ 
	mt[0]=s&0xffffffff;
	for(mti=1;mti<N;mti++)
	{ 
		mt[mti]= (1812433253UL*(mt[mti-1]^(mt[mti-1]>>30))+mti); /*SeeKnuthTAOCPVol2.3rdEd.P.106formultiplier.*//*Inthepreviousversions,MSBsoftheseedaffect*//*onlyMSBsofthearraymt[].*//*2002/01/09modifiedbyMakotoMatsumoto*/
		mt[mti]&=0xffffffffUL;//和这个数进行异或  确定得到的位数是32位的数 
		} 
} 
		
		
/*initialize by  an array  with  array-length*/
/*init_key is  the  array  for  initializing  keys*/
/*key_length is its length*/  
void init_by_array(unsigned long init_key[],int key_length)
{ 
		int i,j,k; 
		init_genrand(19650218UL);//用一个种子对数组进行初始化。 
		i=1;
		j=0; 
		k=(N>key_length?N:key_length);// 
		for(;k;k--)
		{ 
		mt[i]=(mt[i]^((mt[i-1]^(mt[i-1]>>30))*1664525UL))+init_key[j]+j;/*nonlinear*/ 
		mt[i]&=0xffffffffUL;/*forWORDSIZE>32machines*/
		i++;j++;
		 if(i>=N)
		 {mt[0]=mt[N-1];i=1;}
		 if(j>=key_length)j=0; 
		} 
		for(k=N-1;k;k--)
		{ mt[i]=(mt[i]^((mt[i-1]^(mt[i-1]>>30))*1566083941UL)) -i;/*nonlinear*/ 
		mt[i]&=0xffffffffUL;/*forWORDSIZE>32machines*/i++;
		if(i>=N)
		{mt[0]=mt[N-1];i=1;} } 
		mt[0]=0x80000000UL;
		/*MSBis1;assuringnon-zeroinitialarray*/ } /*generatesarandomnumberon[0,0xffffffff]-interval*/
unsigned long genrand_int32(void) 
{ 
unsigned long y; 
static unsigned long mag01[2]={0x0UL,MATRIX_A};
/*mag01[x]=x*MATRIX_A  for  x=0,1*/ 
if(mti>=N) {/*generate  N  word  sat  one  time*/ 
int kk; 
if(mti==N+1)/*if init_genrand()  has  not  been called,*/ 
init_genrand(5489UL);/*a default initial seed  isused*/
for(kk=0;kk<N-M;kk++)
{ 
y=(mt[kk]&UPPER_MASK)|(mt[kk+1]&LOWER_MASK);//实现了伪码中的对y的初始化。 
mt[kk]=mt[kk+M]^(y>>1)^mag01[y&0x1UL];
 } for(;kk<N-1;kk++)
 { y=(mt[kk]&UPPER_MASK)|(mt[kk+1]&LOWER_MASK); 
 mt[kk]=mt[kk+(M-N)]^(y>>1)^mag01[y&0x1UL]; 
 } 
 y=(mt[N-1]&UPPER_MASK)|(mt[0]&LOWER_MASK);
  mt[N-1]=mt[M-1]^(y>>1)^mag01[y&0x1UL];mti=0; } 
  y=mt[mti++]; /*Tempering*/
y^=(y>>11);
y^=(y<<7)&0x9d2c5680UL;
y^=(y<<15)&0xefc60000UL;
y^=(y>>18);
return y; 
}
int main(void){ 
int i;
unsigned long init[4]={0x123,0x234,0x345,0x456},length=4;
init_by_array(init,length);
printf("1000 outputs of genrand_int32()\n");
for(i=0;i<20;i++)
{ 
printf("%10lu\n",genrand_int32()); 
}
}
