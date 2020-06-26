"""
Timmy wants to walk his pet dog twice a day.
He decides that the second walk has to be
6 hours after the first walk ends.
Each walk takes exactly 1 hour.

Timmy is forgetful, so he decides to write
a program that tells him whether or not it
is time to walk his dog a second time.

Write a program that takes the input of
the hour and the minute when the first walk
started and the current time, and prints "Late"
if it is past the scheduled time for the second walk,
"Now" if it is exactly the right time, and
"Early" if it is before the second walk time.

Assume all inputs and outputs must be in 24-hour
style (e.g. 4 PM is 16:00), and that Timmy will schedule
his walks so that the second walk will not start later
than midnight (24:00).
"""

# prompt user for first walk start time
first_hour = int(input('Enter the hour of the time of the first walk: '))
first_minute = int(input('Enter the minute of the time of the first walk: '))

# calculate second walk start time
# add first_hour + 1 is when the first walk ends,
# 6 hours later the second walk should start
second_hour = first_hour + 1 + 6
second_minute = first_minute

# prompt user for current time
current_hour = int(input('Enter the current hour: '))
current_minute = int(input('Enter the current minute: '))

# print whether Timmy is late or early
# to the second walk
if current_hour > second_hour:
    print('Late')
elif current_hour < second_hour:
    print('Early')
else:
    # compare minutes if hours are equal
    if current_minute > second_minute:
        print('Late')
    elif current_minute < second_minute:
        print('Early')
    else:  # current_minute == second_minute
        print('Now')
