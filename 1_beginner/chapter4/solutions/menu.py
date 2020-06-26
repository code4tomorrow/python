food = input("Enter food order: ")
drink = input("Enter drink order: ")
price = 1000000000
if(food == 'french toast' and drink == 'coffee'):
    price = price - 1
elif(food == 'chicken soup' or drink == 'apple juice'):
    price = price + 1

print('The total price is $' + str(price))
