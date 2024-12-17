from Crypto.Util.number import long_to_bytes, inverse
from gmpy2 import iroot
from itertools import combinations


def load_output():
    ret = {"n": [], "c": []}
    with open("output.txt", "rb") as fd:
        while True:
            line = fd.readline()
            if not line:
                break
            line = line.strip().decode()
            if not line:
                continue

            k, v = line.split("=")
            k = k.strip()
            if k == "e":
                continue
            ret[k].append(int(v))

    return ret


def decrypt(grps, e):
    for grp in combinations(zip(grps["n"], grps["c"]), e):
        N = 1
        for x in grp:
            N *= x[0]

        M = 0
        for x in grp:
            M += x[1] * inverse(N // x[0], x[0]) * (N // x[0])
        M %= N

        m, exact = iroot(M, e)
        if exact:
            print(long_to_bytes(m))


# Reference
# [Hastad’s Broadcast Attack](https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-2/)

crt = load_output()
for three in combinations(zip(crt["n"], crt["c"]), 3):
    N = 1
    M_3 = 0
    for n in three:
        N *= n[0]

    for n in three:
        M_3 += n[1] * (N // n[0]) * inverse(N // n[0], n[0])

    M_3 %= N

    m, exact = iroot(M_3, 3)
    if exact:
        print(long_to_bytes(m).decode())
