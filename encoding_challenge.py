from pwn import * # pip install pwntools
from Crypto.Util.number import *
from Crypto.Util.number import long_to_bytes
from Crypto import *
from binascii import unhexlify
import codecs 
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
	line = r.recvline()
	return json.loads(line.decode())

def json_send(hsh):
	request = json.dumps(hsh).encode()
	r.sendline(request)

while(1) :

	received = json_recv()

	encoding = received["type"]
	encoded = received["encoded"]
	print("Received type: ")
	print(received["type"])
	print("Received encoded value: ")
	print(received["encoded"])

	if encoding == "base64":
		decoded = base64.b64decode(encoded) # WORKING
		decoded = decoded.decode()
	elif encoding == "hex":
		decoded = bytes.fromhex(encoded)  #WORKING
		decoded = decoded.decode()
	elif encoding == "rot13":
		decoded = codecs.decode(encoded, 'rot_13') #WORKING
	elif encoding == "bigint":
		#decoded = unhexlify(encoded.replace("0x", "")).decode('utf8').replace("'", '"')
		decoded = long_to_bytes(int(encoded, 16)).decode()
	elif encoding == "utf-8":
		decoded = [chr(b) for b in encoded]
		decoded = ''.join(decoded)

	
	print("Decode value is : " + str(decoded))
	to_send = {
		"decoded": decoded
	}
	json_send(to_send)

