"""Intro Task 2
Fish names
"""

fish = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john dory",
        "red cod"]

print("a. First letter of each fish name on a new line:")
for item in fish:
    print(item[0])

print("\nb. First 3 letters of each fish on a new line:")
for item in fish:
    print(item[:3])

print("\nc. The longest fish name is")
largest = ""
for item in fish:
    if len(item) > len(largest):
        largest = item
print(largest)

print("\nd. Fish names which are longer than 1 word:")
for item in fish:
    if " " in item:
        print(item)

print("\ne. Fish names which contain the word cod")
for item in fish:
    if "cod" in item:
        print(item)
