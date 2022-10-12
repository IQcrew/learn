from crypting_machine import encrypt,decrypt


x = input("zadaj spravu: ")

for i in range(10):
    l = encrypt(x)
    print(l)
    
