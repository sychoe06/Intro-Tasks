"""Sandwich maker program
Online Sandwich store that allows users to select ingredients to make their
own sandwich
"""


def order():
    total = 0
    bread = ""
    meat = ""
    garnish = ""
    print("Welcome to the Online Sandwich Store")

    print("\nBread Options:\nwm - wholemeal\nw - white\ncw - cheesy white\n"
          "gf - gluten free")
    while total == 0:
        bread = input("Please select your bread: ").lower()
        if bread == "wm":
            total += 1
            bread = "wholemeal"
        elif bread == "w":
            total += 0.8
            bread = "white"
        elif bread == "cw":
            total += 1.2
            bread = "cheesy white"
        elif bread == "gf":
            total += 1.4
            bread = "gluten free"
        else:
            print("That is not an option! Try again!\n")
    print("- - -")

    print("Meat Options:\nc - chicken\nb - beef\ns - salami\n"
          "v - vegan slice")
    while total < 1.5:
        meat = input("Please select your meat: ").lower()
        if meat == "c":
            total += 2.69
            meat = "chicken"
        elif meat == "b":
            total += 3
            meat = "beef"
        elif meat == "s":
            total += 4
            meat = "salami"
        elif meat == "v":
            total += 3.30
            meat = "vegan slice"
        else:
            print("That is not an option! Try again!\n")
    print("- - -")

    print("Garnish Options:\no - onion\nt - tomato\nl - lettuce\n"
          "c - cheese")
    while total < 6:
        garnish = input("Please select your garnish: ").lower()
        if garnish == "o":
            total += 2.69
            garnish = "onion"
        elif garnish == "t":
            total += 3
            garnish = "tomato"
        elif garnish == "l":
            total += 4
            garnish = "lettuce"
        elif garnish == "c":
            total += 3.30
            garnish = "cheese"
        else:
            print("That is not an option! Try again!\n")

    print("\n--------------\n")
    print("Your sandwich order:\nBread:", bread, "\nMeat:", meat, "\nGarnish:",
          garnish)
    print(f"Total cost: ${total:.2f}")


order()
confirm = "M"
while confirm == "M":
    confirm = input("\nPress 'C' to confirm your order or 'M' to make "
                    "changes: ").upper()
    if confirm == "C":
        print("Your order has been accepted\nThank you for ordering at the "
              "Online Sandwich Store!")
    else:
        print()
        order()

