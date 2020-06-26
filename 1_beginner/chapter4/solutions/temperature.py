temp = int(input("Enter temperature: ")) #possible input range is 0-100

if(60 <= temp <= 100): #60-100 is hot
    print('hot')
if(30 <= temp < 60): #30-59 is normal
    print('normal')
if(0 <= temp < 30): #0-29 is cold
    print('cold')

#alternatively, you can also use elif
