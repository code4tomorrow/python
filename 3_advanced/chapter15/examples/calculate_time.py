# This code will get all the odd birthdays and print it
birthdays = [12, 4, 21, 11, 24]  # O(1)

odd_birthdays = []  # O(1)
for birthday in birthdays:  # O(n)
    if birthday % 2 == 1:  # O(1)*O(n) = O(n)
        odd_birthdays.append(birthday)  # O(1)*O(n) = O(n)

print(odd_birthdays)  # O(1)

# Sum = O(1) + O(1) + O(n) + O(n) + O(n) + O(1)
# Sum = 3*O(1) + 3*O(n)
# Final Running Time = O(n)
