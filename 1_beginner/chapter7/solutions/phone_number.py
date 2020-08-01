"""
Phone Number

Write a program that asks the user to input a phone number.
Strip their input to get rid of any accidental spaces.

If the input has anything besides digits or the input
isn’t exactly 10 digits long, The program should keep asking them
for a phone number until the input is formatted correctly.

Display the phone number at the end.

Example program run:
Enter a phone number (10 digits): 732-000-0000
Enter a phone number (10 digits): abcdeabcde
Enter a phone number (10 digits): (908)9999999
Enter a phone number (10 digits): 732000000
Enter a phone number (10 digits): 1234567891
Your number is 1234567891
"""

number = ""
while len(number) != 10 or not number.isdigit():
    number = input("Enter a phone number (10 digits): ")

print("Your number is", number)
