user_input = input("zadaj cosi: ")
nunms,  operations = "0123456789", "+-*/"
def read(user_input):
    user_input, temp_value, temp_operation = list(user_input.split()), 0.0, "+"
    for i in range(len(user_input)):
        if user_input[i][0] in nunms:
            for num in user_input[i]:
                if num not in nunms:
                    return "wrong input"
            if temp_operation == "+":
                temp_value += float(user_input[i])
            elif temp_operation == "-":
                temp_value -= float(user_input[i])
            elif temp_operation == "/":
                user_input[i] = float(user_input[i-2])/float(user_input[i])
            elif temp_operation == "*":
                temp_value = temp_value*float(user_input[i])
        elif user_input[i] in operations:
            temp_operation = user_input[i]
        else:
            return "wrong input"
    return temp_value
print(read(user_input))