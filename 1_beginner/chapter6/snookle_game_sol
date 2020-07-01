nums = [3,1,4,2,6,5,8,10]
main = 7

choice = ''
win = False       #The game keeps going until this variable is set to True

while (not win): 
    for i in nums:
        print('main number is currently ' + str(main)) #this is optional, but it's easier for the players since they won't have to keep track of the math
        choice = input("[add] or [subtract] " + str(i) + "?\n> ") #text is also optional, I just added it to make it more user-friendly
        if(choice == 'add'):  #The user chooses to add
            main += i         #update main value
        elif(choice == 'subtract'): #The user chooses to subtract
            main -= i         #update main value
        if(main == 12):       #If the main number if 12, the user has won!
            win = True        #This will make the program exit out of the while loop, thus ending the game
            break             #This takes us out of the for loop and straight to the while statement

print('Congrats you won the game!')
