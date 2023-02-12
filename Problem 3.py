"""Intro Task 3
Sentence
"""

count = 0
sentence = input("Enter a sentence: ")
for letter in sentence:
    if letter == "e":
        count += 1
print(count)
