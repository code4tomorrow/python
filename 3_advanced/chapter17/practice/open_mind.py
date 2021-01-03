"""
Two brothers come together to watch TV everyday.
On weekdays(monday through thursday), they are
not open minded and only watch what they like to
watch themselves. Due to this, it is possible
for nothing to be watched. On weekends(friday
through sunday), they are open minded and would
watch what they themselves like to watch and what
the others like to watch even if they themselves
don’t like to watch that specific TV show.
Assume, all the TV shows the brothers like will
be played everyday. Given a day(1-4 represents
weekday and 5-7 represents weekend) and two
sets(what the brothers each like to watch),
return the set of possible TV shows the brothers
would both watch on that day.
"""

def open_mind(first_bro_set, second_bro_set, day):
    pass
    # Remove pass and write your code in here

first_bro_set = {"pokemon", "regular show", "ben 10", 
                 "adventure time", "mega man"}
second_bro_set = {"ben 10", "powerpuff girls",
                  "curious george", "arthur", "mega man"}
print(open_mind(first_bro_set, second_bro_set, 3))
print(open_mind(first_bro_set, second_bro_set, 7))
