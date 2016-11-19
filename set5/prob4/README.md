## Problem 36.Implement Secure Remote Password (SRP)
	Implement Secure Remote Password (SRP)

### 0x01 Question
模拟构建SRP系统，模拟客户端与服务端进行认证
认证成功则OK
### 0x02 Step （main code）
服务端根据password生成v
```
def server(P):
```
客户端与服务端分别生成A，B进行交换
```
def client2Server(g, a, N):
def server2Client(k, v, g, b, N):
```
服务端与客户端由加盐后的password生成sha256
```
def sAndC(salt, P):
```
然后客户端生成S，HMAC-SHA256后发送给服务端
```
def clientGen(k, salt, P, B, g, a, u, N):
def clientSend(C_K, salt):
```
服务端验证收到的HMAC-SHA256,通过则发OK
```
def serverRecive(S_K, salt):
def serverCheck(C2S, S2C):
```

### 0x03 What's the point
了解SRP的验证过程

### 0x04 Reference


