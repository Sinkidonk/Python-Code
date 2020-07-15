## ex 3.17 Encrypt and Decrypt
## scrambleTest.py
## Alex Parys
## 2/3/2019


from scramble2Encrypt import *
from scramble2Decrypt import *
encryptThis="The Quick Brown Fox Jumps Over the Lazy Dog"

print(scramble2Encrypt(encryptThis))
Encrypt = scramble2Encrypt(encryptThis)
print(scramble2Decrypt(Encrypt))
