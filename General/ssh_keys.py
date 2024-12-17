from Crypto.PublicKey import RSA

# SSH 공개 키 파일 읽기
with open("bruce_rsa.pub", "rb") as f:
    ssh_key_data = f.read()

# 공개 키 로드
rsa_key = RSA.import_key(ssh_key_data)

# RSA 키에서 n과 e 추출
n = rsa_key.n  # 모듈러스 n
e = rsa_key.e  # 공개 지수 e

# 결과 출력
print(f"Modulus (n): {n}")
print(f"Public Exponent (e): {e}")

