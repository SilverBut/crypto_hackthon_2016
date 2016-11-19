#! /usr/bin/python3

import challenge33_iDH
import challenge36_SRP

if __name__ == '__main__':
    # login without password
    P = ''
    v, salt = challenge36_SRP.server(challenge36_SRP.P)
    # the client send 0 as its "A" value
    # the client send N, N*2, &c.
    A = [0, challenge36_SRP.N, challenge36_SRP.N*2]
    B = challenge36_SRP.server2Client(challenge36_SRP.k, v, challenge33_iDH.g, challenge33_iDH.b, challenge36_SRP.N)
    for a in A:
        print('a:', a)
        u = challenge36_SRP.sAndC(a, B)
        x, C_K, C_S = challenge36_SRP.clientGen(challenge36_SRP.k, salt, P, B, challenge33_iDH.g, challenge33_iDH.a, u, challenge36_SRP.N)
        print('C_S:', C_S)
        S_S, S_K = challenge36_SRP.serverGen(a, v, u, challenge33_iDH.b, challenge36_SRP.N)
        print('S_S:', S_S)
        C2S = challenge36_SRP.clientSend(C_K, salt)
        S2C = challenge36_SRP.serverRecive(S_K, salt)
        challenge36_SRP.serverCheck(C2S, S2C)

