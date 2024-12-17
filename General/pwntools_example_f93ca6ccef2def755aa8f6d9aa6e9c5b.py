from pwn import *  # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote("socket.cryptohack.org", 13377, level="debug")


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(100):
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    to_send = {"decoded": "changeme"}
    x = ""
    s = received["type"]
    if s == "base64":
        x = base64.b64decode(received["encoded"]).decode()
    elif s == "hex":
        x = str(bytes.fromhex(received["encoded"]), "utf-8")
    elif s == "rot13":
        x = codecs.decode(received["encoded"], "rot_13")
    elif s == "bigint":
        x = str(long_to_bytes(int(received["encoded"], 0)), "utf-8")
    elif s == "utf-8":
        x = "".join([chr(b) for b in received["encoded"]])

    to_send["decoded"] = x
    json_send(to_send)

received = json_recv()
print(received["flag"])
