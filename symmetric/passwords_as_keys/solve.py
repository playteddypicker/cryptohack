from Crypto.Cipher import AES
import hashlib


def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted


c = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

with open("words.txt", "r") as f:
    words = [w.strip() for w in f.readlines()]

for w in words:
    p = hashlib.md5(w.encode()).hexdigest()
    plain = decrypt(c, p)
    if b"crypto" in plain:
        print(plain)
        print(p)
