# Create a program that asks the user to input an integer. Try to
# convert it from a string to an integer. If it fails, send the
# user a message telling them to input a real integer next time

def int_checker():
  number = input("Please input an integer")
  try:
    number = int(number)
  except:
    print("Sorry, that wasn't a valid integer")

int_checker()
