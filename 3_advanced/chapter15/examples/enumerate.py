# The enumerate function assigns numbers to every element
# in an iterable, starting with zero.
# it returns an enumerate object, so you have to do list or tuple
# to access the enumerated values.


countries = ["Japan", "America", "South Korea", "China"]
numerated_list = list(enumerate(countries))
print(numerated_list)
# prints [(0, ' Japan'), (1, 'America'), (2, 'South Korea'), (3, ' China')]


# This code gets all the countries with even indexes greater than 1
answer_list = []
for index, country in enumerate(countries):
    if index % 2 == 0 and index > 1:
        answer_list.append(country)
print(answer_list)
# prints ['South Korea']
