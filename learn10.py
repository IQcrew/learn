import itertools

def accuracy_calc(quote, user_input):
    correct = 0
    for i in range(len(quote.split(" "))):
        try:
            if quote.split(" ")[i] == user_input.split(" ")[i]:
                correct += 1
        except: pass
    return correct/len(quote.split(" "))*100


print(accuracy_calc("hi my name is cat, and idk", "hi my name is cat, nda ijkd"))