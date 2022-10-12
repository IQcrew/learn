input_month = input("Write month: ").lower()
try: input_day = int(input("Write day: "))
except: input_day = -1
def writeSeason(Imont : str, Iday : int):
    months = {
        "Spring" : {"march" :(20,31), "april" : (1,30), "may" : (1,31), "june" : (0,20)},
        "Summer" : {"june" :(21,30), "july" : (1,31), "august" : (1,31), "september" : (0,21)},
        "Autumn" : {"september" :(22,30), "october" : (1,31), "november" : (1,30), "december" : (0,20)},
        "Winter" : {"december" :(21,31), "january" : (1,31), "february" : (1,29), "march" : (0,19)},}
    for season in months.keys():
        for month in months[season].keys():
            if(month == Imont and months[season][month][0]<=Iday and months[season][month][1]>=Iday):
                return season
    return "Invalid"
print(writeSeason(input_month,input_day))