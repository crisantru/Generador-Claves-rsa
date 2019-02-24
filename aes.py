from Crypto.Cipher import AES
from Crypto import Random

key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
print(Random.new())

obj = AES.new(key, AES.MODE_CFB, iv)
message = "La chica club, su primer amor"
print(len(message))
ciphertext = obj.encrypt(message)

print(ciphertext)

obj2 = AES.new(key, AES.MODE_CFB, iv)
mensaje_recuperado = str(obj2.decrypt(ciphertext))
print(mensaje_recuperado)