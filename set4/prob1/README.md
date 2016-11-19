# Problem 25. Break "random access read/write" AES CTR

### 0x01 Question

攻击者知道密文，有一个可以对密文对应的明文任意写的api，要求仅通过这些来回复出明文

### 0x02 Step （main code）

攻击者只要修改明文全部为'\x00'即可得到keystream，得到的keystream和ciphertext异或即可恢复出明文

### 0x03 What's the point


### 0x04 Reference


