a = 288260533169915
p = 1007621497415251


def tonelli_shanks(n, p):
    def isQR(x, p):
        return pow(x, (p - 1) // 2, p) == 1

    if not isQR(n, p):
        return -1
    Q, S = p - 1, 0
    while Q % 2 == 0:
        S += 1
        Q //= 2
    z = None
    for x in range(2, p):
        if not isQR(x, p):
            z = x
            break
    M, c, t, R = S, pow(z, Q, p), pow(n, Q, p), pow(n, (Q + 1) // 2, p)
    while True:
        if t == 0:
            return 0
        elif t == 1:
            return R
        k = t * t % p
        ii = None
        for i in range(1, M):
            if k == 1:
                ii = i
                break
            k *= k
            k %= p
        b = pow(c, 2 ** (M - i - 1), p) % p
        M = ii % p
        c = b * b % p
        t = t * c % p
        R = R * b % p


print(pow(a, (p - 1) // 2, p))
if pow(a, (p - 1) // 2, p) == 1:
    print(tonelli_shanks(a, p))