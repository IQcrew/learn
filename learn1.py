import random
def priemer(list_numbers):
    temp_value = 0.0
    for i in range(len(list_numbers)):
        temp_value += list_numbers[i]
    return (temp_value/len(list_numbers))
list_of_numbers = []
for i in range(100):
    list_of_numbers.append(random.randrange(0,6))
print(priemer(list_of_numbers))