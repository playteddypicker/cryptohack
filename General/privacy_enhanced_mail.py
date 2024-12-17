from Crypto.PublicKey import RSA

with open("privacy_enhanced_mail.pem", "rb") as pem_file:
    pem_data = pem_file.read()

key = RSA.importKey(pem_data)

print(f"d (private key): {key.d}")

