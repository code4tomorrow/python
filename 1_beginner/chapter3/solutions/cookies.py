"""
Cookies
Prompt the user with the following questions:
  How many cookies did you make?
  How many cookies did your friend make?
  How many cookies are burnt?
  How many friends do you have?

Print the total number of unburnt cookies.
Then output the number of cookies that will be left over if you
throw out all the burnt cookies and all the friends get the same amount.
"""

# Get all the inputs and store as integers in variables
your_cookies = int(input("How many cookies did you make? "))
friend_cookies = int(input("How many cookies did your friend make? "))
burnt_cookies = int(input("How many of those cookies are burnt? "))
friend_count = int(input("How many friends do you have? "))
print()  # This makes a new empty line (a line break)

# Calculate the total number of unburnt cookies
total = your_cookies + friend_cookies - burnt_cookies

# Display the number of unburnt cookies.
# Cast the integer variable "total" to a string
print("Number of unburnt cookies: " + str(total))

# Calculate the REMAINDER of cookies
# after dividing the total between your friends
remainder = total % friend_count

# Display the number of cookies left over
print("Number of cookies left over:", remainder)
