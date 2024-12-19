from pwn import *
import json
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

# 서버 연결
host = "socket.cryptohack.org"
port = 13386
io = remote(host, port)

# 대화형 모드로 전환
io.sendlineafter(b"flag.\n", '{"option": "get_flag"}')
response = io.recvline()

data = json.loads(response.decode())

print(data)

encrypted_flag = int(data["encrypted_flag"])
modulus = int(data["modulus"])
a, b = data["padding"]

# 1. 암호문 복호화 (e-th root)
m_padded, exact = iroot(encrypted_flag, 11)
assert exact, "Decryption failed!"

# 2. 패딩 제거
m = (m_padded - b) // a

# 3. 플래그 복구
flag = long_to_bytes(m)
print("Recovered Flag:", flag.decode())
