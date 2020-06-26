first_hour = int(input('Enter the hour of the time of the first walk: '))
first_minute = int(input('Enter the minute of the time of the first walk: '))

second_hour = first_hour + 1 + 6 #add first_hour + 1 is when the first walk ends, 6 hours later the second walk should start
second_minute = first_minute

current_hour = int(input('Enter the current hour: '))
current_minute = int(input('Enter the current minute: '))

if(current_hour > second_hour):
    print('Late')
elif(current_hour < second_hour):
    print('Early')
else: #current_hour == second_hour
    if(current_minute > second_minute):
        print('Late')
    elif(current_minute < second_minute):
        print('Early')
    else: #current_minute == second_minute
        print('Now')
