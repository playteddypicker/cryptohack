from Crypto.PublicKey import RSA

# DER 파일 읽기
with open("2048b-rsa-example.der", "rb") as der_file:
    der_data = der_file.read()

# RSA 키 로드
key = RSA.importKey(der_data)

# 모듈러스 n 출력
print(f"Modulus (n): {key.n}")
