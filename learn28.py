import crypting_machine
with open("data.txt", "w") as f:
    x = "a"*10000
    f.writelines(x)

x = crypting_machine.encrypt(x)
print(x)
x = crypting_machine.decrypt(x)
print(x)
with open("data.txt", "w") as f:
    f.writelines(x)

