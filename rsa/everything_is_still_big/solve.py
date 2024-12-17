from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Util.number import long_to_bytes
from base64 import b64decode, b64encode

with open("private_key.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

c = 0xA3BCE6E2E677D7855A1A7819EB1879779D1E1EEFA21A1A6E205C8B46FDC020A2487FDD07DBAE99274204FADDA2BA69AF73627BDDDCB2C403118F507BCA03CB0BAD7A8CD03F70DEFC31FA904D71230AAB98A10E155BF207DA1B1CAC1503F48CAB3758024CC6E62AFE99767E9E4C151B75F60D8F7989C152FDF4FF4B95CEED9A7065F38C68DEE4DD0DA503650D3246D463F504B36E1D6FAFABB35D2390ECF0419B2BB67C4C647FB38511B34EB494D9289C872203FA70F4084D2FA2367A63A8881B74CC38730AD7584328DE6A7D92E4CA18098A15119BAEE91237CEA24975BDFC19BDBCE7C1559899A88125935584CD37C8DD31F3F2B4517EEFAE84E7E588344FA5

cipher = PKCS1_v1_5.new(private_key)
m = pow(c, private_key.d, private_key.n)

print(long_to_bytes(m))