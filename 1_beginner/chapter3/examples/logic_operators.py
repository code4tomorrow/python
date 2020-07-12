# Logic Operators

# and
were_cookies_bought = True
were_chips_bought = True
print(
    "Were both cookies and chips bought? "
    + str(were_cookies_bought and were_chips_bought)
)

# or
was_computer_bought = True
was_bike_bought = False
print("Was a computer or bike bought? "
      + str(was_computer_bought or was_bike_bought))

# not
is_raining = False
print("Is it NOT raining? " + str(not is_raining))
