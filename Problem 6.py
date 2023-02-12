"""Intro Task 6
Find the largest number in the list
"""

numbers = [20, 36, 12, 24, 20, 48, 74, 353, 23, 98]
new_num = 0
for num in numbers:
    if num > new_num:
        new_num = num
print("The largest number in this list is", new_num)
