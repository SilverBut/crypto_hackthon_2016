## Problem <21>.<Implement the MT19937 Mersenne Twister RNG>
问题的要求是实现梅森旋转算法，在维基百科上有具体的伪代码。
算法实现的步骤如下
### 0x01
按照维基百科上的伪码进行分析，先确定一个seed,然后用seed初始化state数组，然后对数组初始化，这个算法中生成了624个随机数。
### 0x03 Reference
参考维基百科上对于梅森旋转算法的伪码。
 //创建一个长度为624的数组来存储发生器的状态
 int[0..623] MT
 int index = 0
 
 //用一个种子初始化发生器
 function initialize_generator(int seed) {
     i := 0
     MT[0] := seed
     for i from 1 to 623 { // 遍历剩下的每个元素
         MT[i] := last 32 bits of(1812433253 * (MT[i-1] xor (right shift by 30 bits(MT[i-1]))) + i) // 0x6c078965
     }
 }
 
 // Extract a tempered pseudorandom number based on the index-th value,
 // calling generate_numbers() every 624 numbers
 function extract_number() {
     if index == 0 {
         generate_numbers()
     }
 
     int y := MT[index]
     y := y xor (right shift by 11 bits(y))
     y := y xor (left shift by 7 bits(y) and (2636928640)) // 0x9d2c5680
     y := y xor (left shift by 15 bits(y) and (4022730752)) // 0xefc60000
     y := y xor (right shift by 18 bits(y))

     index := (index + 1) mod 624
     return y
 }
 
 // Generate an array of 624 untempered numbers
 function generate_numbers() {
     for i from 0 to 623 {
         int y := (MT[i] & 0x80000000)                       // bit 31 (32nd bit) of MT[i]
                        + (MT[(i+1) mod 624] & 0x7fffffff)   // bits 0-30 (first 31 bits) of MT[...]
         MT[i] := MT[(i + 397) mod 624] xor (right shift by 1 bit(y))
         if (y mod 2) != 0 { // y is odd
             MT[i] := MT[i] xor (2567483615) // 0x9908b0df
         }
     }
 }
