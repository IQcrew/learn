from numpy import alen
from crypting_machine import decrypt, encrypt
user_input = input('Enter string to crypt: ')
print("encrypted: ÷", end="")
print(encrypt(user_input))
print("÷decrypted: ¤",end="")
print(decrypt(user_input)+"¤")