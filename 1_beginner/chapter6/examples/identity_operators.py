# Identity Operators

message_1 = 'hello'
message_2 = 'hello'

print(message_1 is message_2)  # True
print(message_1 is not message_2)  # False

message_3 = 'world'
message_4 = 'tahiti'

print(message_3 is message_4)  # False
print(message_3 is not message_4)  # True

# Identity vs Equality

# primitive values, if duplicated,
# are stored in the same location
x = 5
y = 5
if x is y:
    print('x is y')
else:
    print('x is not y')

# lists are objects,
# so they are located in different
# locations in memory
a = [1, 2, 3]
b = [1, 2, 3]

# use the identity operator
# to test if the 2 variables
# reference the same location
# in memory
if a is b:
    print('a is b')
else:
    print('a is not b')

# use the equality operator
# to test if content is equivalent
if a == b:
    print('a == b')
else:
    print('a != b')
