## Problem 37.Break SRP with a zero key
	Break SRP with a zero key
### 0x01 Question
log in without your password by having the client send 0 as its "A" value.What does this to the "S" value that both sides compute?
And then N, N*2, &c.
### 0x02 Step
仍由服务端生成salt和v
```
v, salt = challenge36_SRP.server(challenge36_SRP.P)
```
A分别为[0, challenge36_SRP.N, challenge36_SRP.N*2]
客户端由空密码生成S
```
x, C_K, C_S = challenge36_SRP.clientGen(challenge36_SRP.k, salt, P, B, challenge33_iDH.g, challenge33_iDH.a, u, challenge36_SRP.N)

```
服务端生成S
```
S_S, S_K = challenge36_SRP.serverGen(a, v, u, challenge33_iDH.b, challenge36_SRP.N)

```
验证是否通过
```
challenge36_SRP.serverCheck(C2S, S2C)
```
### 0x03 the Point
当A为0, N， N*2时，服务端S一直为0
问题：c是哪个？
### Reference
