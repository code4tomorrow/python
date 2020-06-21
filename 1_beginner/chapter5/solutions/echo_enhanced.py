# Echo Enhanced
# Write a program that continuously prompts the user
# to enter a message, and echoes that message
# back to the user (prints it). If the message
# is 'q', the program should end. If the message is
# 'c', the program shouldn't echo anything but instead
# prompt the user to enter another message to echo.
# See a demo of the program here: https://youtu.be/Rb5LUiXzAcU

print("Enter a message, 'c' to cancel an echo, or 'q' to quit.")
while True:
    message = input("Message: ")
    if message == 'q':
        break  # quit
    elif message == 'c':
        continue  # cancel echo
    else:
        print(message)  # echo message
