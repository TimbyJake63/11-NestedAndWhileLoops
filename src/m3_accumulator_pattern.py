###############################################################################
# DONE: 1. (3 pts)
#
#   For this _TODO_, write a block of code that uses the list of numbers defined below and calculates the sum of all the numbers.
#
#   You may use whatever type of loop you wish, but you must use the accumulator pattern in your solution. So, you should have at least one variable that you use to accumulate information as you go.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Total= 0
for x in nums:
    Total += x
print(Total)
###############################################################################
# DONE: 2. (3 pts)
#
#   For this _TODO_, write a block of code that uses the string defined below and counts how many characters are in the string.
#
#   DO NOT use len() in your solution.
#
#   You may use whatever type of loop you wish, but you must use the accumulator pattern in your solution. So, you should have at least one variable that you use to accumulate information as you go.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
txt = "The quick brown fox jumps over the lazy dog."

count = 0
for x in txt:
    count += 1
print(count)