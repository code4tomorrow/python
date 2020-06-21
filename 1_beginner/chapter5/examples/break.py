# Break
x = int(input("Enter a number: "))
while x < 20:
    # break out of loop if
    # current is divisible by 4
    if x % 4 == 0:
        break
    print(x)
    x += 1
