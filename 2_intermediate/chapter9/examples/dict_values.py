# Retrieving, Updating, and Adding Values

contacts = {
    "John Doe": "1234 Main St",
    "Jane Smith": "5678 Market St",
    "Daisy Johnson": "1357 Wall St"
}

daisy_address = contacts["Daisy Johnson"]
print(daisy_address)  # prints “1357 Wall St”

contacts["Daisy Johnson"] = "2468 Park Ave"
print(contacts["Daisy Johnson"])  # prints “2468 Park Ave”

contacts["Leo Fitz"] = "1258 Monkey Dr"
print(contacts)  # prints the dictionary with the new entry
