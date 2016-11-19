## Problem <problem 22>.<Crack an MT19937 seed>
题目描述：
对MT19937的种子进行攻击
确保你的MT19937接受一个整数种子值，测试这个种子:确保在每次输入种子的时候得到的是相同的序列。
写一个流程来实现接下来的操作：
1：等待一个随机的在40到1000之间的秒数
2：使用当前的unix时间戳为RNG生成种子。
3：再次等待一个随机的秒数
4：返回RNG前32位输出。
RNG是随机数生成器。从32比特的RNG输出中，得到了种子。

### 0x01
函数中有一个遍历的问题：
第一步：随机生成一个秒数，然后将当前的时间作为时间戳放进seed中，然后再等待一个时间
第二步：想要验证相同的seed获得相同的输出，只能使用很多个时间戳了
第一对时间戳执行从程序开始执行到程序输出一个随机的
第二对，第三对时间戳 就是单纯用来生成种子的
### 0x02
分析：函数中的问题是：不便于对于时间戳函数进行处理。c语言直接的函数库不太对劲
函数实现的方式是利用3对时间之间的差值来进行转化，但是时间戳转化为int型函数很不友好。
int i;
	time_t *stime,*etime;//用来遍历寻找刚刚的seed的值。 
	time(stime);
	int wtime=rand()%960+40;
	time_t *stime2,*etime2;
	time_t *time3; 
    int seed;
	time(stime2);
	printf("%d",stime);
	while(1){
		time(etime2); 
		if(etime2-stime2>wtime){
			break;
		}
	}
	time(time3);
	seed=difftime(time3);
	init_PRG(seed);
	int prg=ext_PRG();
	time(stime2);
	wtime=rand()%960+40;
	time(stime2);
	while(1){
		time(etime2);
		if((etime2-stime2)>wtime){
			break;
		}
	} 
	time(etime);
	for(i=stime;i<etime;i++){
		init_PRG(i);
		if(ext_PRG()==prg){
			break;
		}
	}
	printf("%d",i);
既然函数是为了验证相同的seed产生相同的随机数，可以直接利用遍历的方式进行处理。
### 0x03 Reference
