import math
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, inverse, bytes_to_long
from Crypto.Cipher import PKCS1_OAEP

public = RSA.importKey(open("key.pem").read())
n = int(public.n)
e = int(public.e)
# got these p, q values from roca_attack.py by FlorianPicca
# https://github.com/FlorianPicca/ROCA/blob/master/roca_attack.py
p = 77342270837753916396402614215980760127245056504361515489809293852222206596161
q = 51894141255108267693828471848483688186015845988173648228318286999011443419469
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
c = 0x249D72CD1D287B1A15A3881F2BFF5788BC4BF62C789F2DF44D88AAE805B54C9A94B8944C0BA798F70062B66160FEE312B98879F1DD5D17B33095FEB3C5830D28

key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)

print(cipher.decrypt(bytes.fromhex(hex(c)[2:])))
