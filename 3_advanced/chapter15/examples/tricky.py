# Tricky if statements
ex_list = [1, 23, 421, 32]
if 1 == 2:
    for num in ex_list:
        print(num)
else:
    print(ex_list)


# Loops ending prematurely
ex_list = [1, 23, 421, 32]
counter = 0
for num in ex_list:
    counter += 1
    print(num)
    if counter == 1:
        break
