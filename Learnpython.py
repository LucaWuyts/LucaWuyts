#Let's build a robot Barista!!

print("Hello, welcome to NetworkChuck Coffee!!!")

name = input("What is your name?\n")


if name == "Ben":
    print("You're not welcome here Evil Ben!! Get out!!")
    exit()
else:
    print("Hello " + name + " ,thank you so much for coming in today!\n\n\n")



menu = "Black Coffee, Espresso, Latte, Cappuccino"

print(name + " ,what would you like from our menu today? Here is what we are serving. \n" + menu)

order = input()

price = 8

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))

print("Sounds good " + name + " ,we'll have your " + quantity + " " + order + " ready for you in a moment.")
