"""Intro Task 4
Two strings
"""


def finding_letter():
    count = 0
    for item in sentence:
        if item == letter:
            count += 1
    print("The letter", letter, "appeared", count, "times in the sentence")


letter = input("Enter a letter: ")
sentence = input("Enter a sentence: ")
finding_letter()
