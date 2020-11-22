"""
Problem Name: darwin_raccoon
Darwin is observing raccoons’ growths on an unnamed island. He spends 7 days 
in total on this island, and on every day, he would record the average growth of 
raccoons in inches. He loses data on day 7, so he decides to make the data on 
that day to be the maximum of the previous 6 days. He needs to make a dictionary 
for use later where the key is the day number and the value is the average growth 
of raccoons on that day. You help him make the dictionary. Use zip to solve this 
problem.
"""

# The lists are already given to you
days_list = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
growths_list = [1.4, 2.1, 1.3, 0.1, 0.4, 1.9]

# write your code below
data_dictionary = dict(zip(days_list, growths_list + [max(growths_list)]))
