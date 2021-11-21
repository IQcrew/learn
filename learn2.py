numbers = "0123456789."
user_input = input("zadaj cosi:  ")
def percent(user_input):
    temp_string, temp_string_2 = "", ""
    for i in range(len(user_input)):
        if user_input[i] == "%":
            for n in range(i-1, -1, -1):
                if user_input[n] in numbers:
                    temp_string += user_input[n]               
        if user_input[i] == "z" and temp_string != "":
            for i in range(i+1,len(user_input)):            
                if user_input[i] in numbers:
                    temp_string_2 += user_input[i]
                elif user_input[i] == " " and temp_string_2 == "":
                    pass
                else:
                    break
            return((float(temp_string[::-1])/100)*float(temp_string_2))
print(percent(user_input))