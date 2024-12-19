from Crypto.PublicKey import RSA
import os
from math import gcd
from Crypto.Util.number import inverse, long_to_bytes
from Crypto.Cipher import PKCS1_OAEP

# n 값을 저장할 리스트
nlist = []

# keys_and_messages 폴더 경로
folder_path = "keys_and_messages"

# 1.pem부터 50.pem까지 읽어오기
for i in range(1, 51):
    file_path = os.path.join(folder_path, f"{i}.pem")
    with open(file_path, "r") as pem_file:
        key = RSA.import_key(pem_file.read())

        n = key.n
        nlist.append((key.n, key.e))

# 결과 출력 (옵션)
p = 1

for i in range(0, 50):
    if i == 20:
        continue
    g = gcd(nlist[i][0], nlist[20][0])
    if g != 1:
        p = g

q = nlist[20][0] // p
e = nlist[20][1]
print(f"p: {p}\nq: {q}")

n = nlist[20][0]
assert p * q == n

phi = (p - 1) * (q - 1)
d = inverse(nlist[20][1], phi)
c = ""
file_path = os.path.join(folder_path, "21.ciphertext")
with open(file_path, "r") as f:
    c = f.read()

key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)
print(cipher.decrypt(bytes.fromhex(c)))
