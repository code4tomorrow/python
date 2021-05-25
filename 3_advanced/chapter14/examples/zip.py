a = [1, 2, 3]
b = ["a", "b", "c"]
c = ["!", "@", "#"]

G = zip(a, b, c)

print(list(G))
# prints [(1, 'a', '!'), (2, 'b', '@'), (3, 'c', '#')]


list_one = [1, 2]
list_two = [41]

for pair in zip(list_one, list_two):
    print(pair)
# this would only print (1, 41)


countries = [" Japan", "America", "South Korea", " China"]
numbers = [1, 2, 3, 4]
dict1 = dict(zip(countries, numbers))
print(dict1)
# prints {' China': 4, ' Japan': 1, 'America': 2, 'South Korea': 3}
