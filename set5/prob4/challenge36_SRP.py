# ! /usr/bin/python3

import challenge33_iDH
import hashlib
from Crypto import Random

# C & S
# Agree on N=[NIST Prime], g=2, k=3, I (email), P (P)
# N = 115792089210356248762697446949407573530086143415290314195533631308867097853951
N = challenge33_iDH.p
k = 3
I = 'yourtest@mail.xidian.com'
P = 'this_is_your_password.'


# S
# Generate salt as random integer
# Generate string xH=SHA256(salt|P)
# Convert xH to integer x somehow (put 0x on hexdigest)
# Generate v=g**x % N
# Save everything but x, xH
def server(P):
    salt = Random.new().read(16)
    xH = hashlib.sha256(salt + bytes(P, 'utf-8'))
    xH = '0x' + xH.hexdigest()
    x = int(xH, 16)
    v = pow(challenge33_iDH.g, x, N)
    return v, salt


# C->S
# Send I, A=g**a % N (a la Diffie Hellman)
def client2Server(g, a, N):
    A = pow(g, a, N)
    return A


# S->C
# Send salt, B=kv + g**b % N
def server2Client(k, v, g, b, N):
    B = k * v + pow(g, b, N)
    return B


# S, C
# Compute string uH = SHA256(A|B), u = integer of uH
def sAndC(A, B):
    uH = hashlib.sha256((str(A) + str(B)).encode())
    u = int(uH.hexdigest(), 16)
    return u


# C
# Generate string xH=SHA256(salt|password)
# Convert xH to integer x somehow (put 0x on hexdigest)
# Generate S = (B - k * g**x)**(a + u * x) % N
# Generate K = SHA256(S)
def clientGen(k, salt, P, B, g, a, u, N):
    xH = hashlib.sha256(salt + bytes(P, 'utf-8'))
    x = int(xH.hexdigest(), 16)
    C_S = pow((B - k * pow(g, x, N)), (a + u * x), N)
    # print('C_S:', C_S)
    C_K = hashlib.sha256(str(C_S).encode()).hexdigest()
    # print('C_K:', C_K)
    return x, C_K, C_S


# S
# Generate S = (A * v**u) ** b % N
# Generate K = SHA256(S)
def serverGen(A, v, u, b, N):
    S_S = pow((A * pow(v, u, N)), b, N)
    S_K = hashlib.sha256(str(S_S).encode()).hexdigest()
    return S_S, S_K


# C->S
# Send HMAC-SHA256(K, salt)
def clientSend(C_K, salt):
    C2S = hashlib.pbkdf2_hmac('sha256', bytes(str(C_K), 'utf-8'), salt, 10000)
    # print('C2S:', C2S)
    return C2S

# S2C generate HMAC-SHA256(K, salt)
def serverRecive(S_K, salt):
    S2C = hashlib.pbkdf2_hmac('sha256', bytes(str(S_K), 'utf-8'), salt, 10000)
    return S2C

# Send "OK" if HMAC-SHA256(K, salt) validates
def serverCheck(C2S, S2C):
    if C2S == S2C:
        print('OK.')
    else:
        print('failed.')


if __name__ == '__main__':
    v, salt = server(P)
    print(v, salt)
    A = client2Server(challenge33_iDH.g, challenge33_iDH.a, N)
    B = server2Client(k, v, challenge33_iDH.g, challenge33_iDH.b, N)
    u = sAndC(A, B)
    x, C_K, C_S = clientGen(k, salt, P, B, challenge33_iDH.g, challenge33_iDH.a, u, N)
    S_S, S_K = serverGen(A, v, u, challenge33_iDH.b, N)
    C2S = clientSend(C_K, salt)
    S2C = serverRecive(S_K, salt)
    print(C2S, S2C)
    serverCheck(C2S, S2C)