# Problem name: add_10
# A messy teacher named Bob would like to add 10 points to each student’s recent test score.
# There are four students, and going from highest score to lowest score, it is Mike, Dan, Stan, and Ban.
# Add 10 to each score and assign those values to the correct student.
# Solve this problem by adding no more than 2 lines of code.
# Hint: Use tuple unpacking and list comprehension.

# the scores are given
scores = (100, 90, 80, 70)

# write your code below
scores_added = [n + 10 for n in scores]
Mike, Dan, Stan, Ban = scores_added
