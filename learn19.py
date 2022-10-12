#Gathering user input for month and day
input_month = input().lower()
input_day = int(input())

#Setting up lists for each month (Only for months that would absolutely tell which season)
spring = ('april', 'may')
summer = ('july', 'august')
autumn = ('october', 'november')
winter = ('january', 'february')

if (input_day > 31 or input_day < 0) or not (input_month in spring or input_month in summer or input_month in autumn or input_month in winter):
    print('Invalid')
else:
    if input_month in spring:
        print('Spring')

    elif input_month in summer:
        print('Summer')
        
    elif input_month in autumn:
        print('Autumn')

    elif input_month in winter:
        print('Winter')

    elif input_month == 'March':
        if input_day < 20:
            print('Winter')
        else:
            print('Spring')

    elif input_month == 'June':
        if input_day >= 21:
            print('Summer')
        else:
            print('Spring')
        
    elif input_month == 'September':
        if input_day <= 21:
            print('Summer')
        else:
            print('Autumn')
            
    elif input_month == 'December':
        if input_day >= 21:
            print('Winter')
        else:
            print('Autumn')