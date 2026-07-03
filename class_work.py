# list_of_items=[]
# print(list_of_items)
# list_of_items2 =["purse", "pen", "bottle"]
# print(list_of_items2)

# # list_of_items2 +=[soap]
# # print(list_of_items2)

# # list_of_items2.append("soap") add the list of item 1 &2 to a single list of items 1
# # print(list_of_items2)

# list_of_items+=[soap]
# print(list_of_items)


# list_of_items = list_of_items + list_of_items2
# print(list_of_items)

# daily_sales = []
# daily_sales = [8.7, 9.7, 6.7,80.3]
# print(daily_sales)

# total = 3
# for sale in daily_sales:
#     total = total + sale

# print(total)
# my_list=[
#     2   0 -9
#     4   1 -8
#     3,  2 -7
#     3,  3 -6
#     6,  4 -5
#     8,  5 -4
#     12, 6 -3
#     14, 7 -2
#     -6  8 -1
#     #9
#     #12 index error
#     #14 index error
# ]

# my_list=[
#     10, 
#     11, 
#     12,
#     13,
#     14,  
#     15,   
#     #5
    
# ]
# print(my_list)
# my_list[1]= my_list[3]

# my_list[1]= my_list[-1] + my_list[3]
# print(my_list[1])

# Core drill: “Create Inventory Records”

# Create a dictionary for one product with:

# name
# selling_price
# quantity
# expiry_date
# Then:
# Read the quantity
# Reduce quantity after a sale
# Update the dictionary

# product ={"name":"milk", "selling_price":2.20, "quantity":50, "expiry_date": "2025/03/11"}
# print(product["quantity"])
# product["quantity"] -=10
# print(product["quantity"])
# print(product)

# # if "name" in product
# product.keys()
# print(product.keys())
# product.values()
# print(product.values())
# for i in product:
#     print(i)
# for i in product.values():
#     print(i)


# Expand on the products, create 3 products using this template
# Day 1 milk 2 units ,water 2 units each, such progress price, what has been sold, the amount made and what is left

# Day 2 bread was sold 3 units, water was sold 1 unit
# Day 3 each item was sold for 4 units
# water having the least amount of supply has 10 units, and bread has double the figures and milk has double what bread has
# add extra field at my own discretion 

# product ={"name":"milk", "selling_price":2.20, "quantity":50, "expiry_date": "2025/03/11"}

# Core drill: “Low Stock Warning”
# Goal: Prove you can enforce rules.
# Scenario from PRD: Owner must be warned when stock is low.
# Exercise:
# Set a low stock threshold
# Check product quantity
# If quantity is below threshold:

# Print “Low stock warning”
# Else:

# Print “Stock level okay”
# low stock

# low_stock = 5
# product_quantity = 10
# expiry_date = "2025/01/16"
# if product_quantity < low_stock:
#     print("low stock warning")
# else:
#         print("stock is okay")
# if expiry_date < "2025/03/01":
#     print("Product expired warning")
# first
# if big popcorn in store, else if small popcorn

# second example
# if big popcorn in store, if small popcorn in store
# big_popcorn = 6
# small_popcorn = 8
# if big_popcorn > 2:
#     print("big popcorn is in store")
# elif big_popcorn < 7:
#     print("small popcorn is in the store")
# if small_popcorn > 4:
#     print("small popcorn is in the store")

# 1, checking for orange and banana and trying to buy both. 
# 2, looking for chanel or versace. pick any one but you can't buy two of them
# 3, buy best brand if not by any other brand
# 4, maximise budget,500, one fan is worth 400, one light bulb is 200, chair 100, end up using money efficiently
# store = ("orange", "banana","chanel","versace")
# if "orange" in store:
#     print("buy orange")
# if "banana" in store:
#     print("buy banana")
#     print("buy both")

# if "chanel" in store:
#     print("buy chanel")
# elif "versace" in store:
#     print("buy versace")

# if "zara" in store:
#     print("buy zara")
# else: 
#     print("buy any other brand")

# budget = 400
# fan = 400
# bulb = 200
# chair = 100

# if budget >= chair:
#     print("buy chair for 100")
#     budget = budget - chair

# if budget >= bulb:
#     print("buy bulb for 200")
#     budget = budget - bulb

# if budget >= fan:
#     print("buy fan for 400")
# #     budget = budget - fan

# # print(budget)
    

# # Core drill: “Check Full Inventory.”
# # Goal: Prove you can apply rules across many records.
# # Scenario from PRD:
# #  The system must scan all products, not one.
# # Exercise:
# # Create a list of product dictionaries
# # Loop through each product
# # Check stock level
# # Print warning only for low-stock items

# # products=[ 
# #     {"name": "milk", "selling_price": 2.20, "quantity": 80},
# #     {"name": "bread", "selling_price": 3.50, "quantity": 410},
# #     {"name": "water", "selling_price": 1.00, "quantity": 10}
# # ]
# # low_stock = 100
# # for product in products:
# #     if product["quantity"] < low_stock:
# #         print("WARNING:", product["name"], "low on stock")

    
# # for k in products [0]:
# #     print(k)
# # print()
# # print("values")

# # for v in products [0].values():
# #     print(v)
# # print()
# # print("keys2")

# # for k in products [0].keys():
# #     print(k)


# # 50 dictionaries and 10 list
# # person ={"name": "onyi", "age": 90, "city": "london"}
# # print(person.keys())
# # print(person.values())
# # n/
# # Bag={"purse": "money","amount": 100, "location": "dubai"}
# # print(Bag.keys())
# # print(Bag.values())

# # channel = {"name": "netflix", "number": 8, "every": "Tuesday"}
# # print(channel.keys())
# # print(channel.values())

# # Heater = {"name":"microwave", "degree": 2}
# # print(Heater.keys())
# # print(Heater.values())

# # product = {"name": "laptop", "price": 999.9, "in_stock": "Yes"}
# # print(product.keys())
# # print(product.values())

# # product={"name": "wavy_curls", "price" 234, "avaliable": "True"}
# # print(product.keys())
# # print(product.values())

# # furniture = {"name": "chair", "price" 45, "shop_location": "Abeokuta"}
# # Baddie = {"name": "onyi", "weight" 73, "specifications": "knees": "not_megan"}
# # book = {"name": "credence", "audience" 18+, "type": "smut"}
# # Car = {"name":"benz", "year" 2026, "colour": "blue"}
# # flower = {"name":"rose", "quantity" 12, "colour": "red"}
# # Gender = {"name": "man", "height" 167, "location": "newyork"}
# # meal = {"name": "noodles", "quantity" 3, "expiry_date" 2026, "in_stock" "yes"} 
# # forecast = {"type": "weather", "degree"2, "part_cloudy": "in_london"}
# # exercise = {"name": "walking_exercies", "sets" 2.2, "where": "park"}
# # notebook = {"name" "writing_pad", "quantity" 50, "where": "in_my_bag"}
# # product ={"name": "bottled_water", "quantity" 4, "in_stock": "True"}


# # 10 list
# # fruits = ("apple", "banana", "kiwi")
# # furniture = ("chair", "lamp", "television")
# # perfumes = ("zara", "chanel", "sunna_musk")
# # name =("onyi", "peter", "Joyce")
# # fonts = ("italic", "roman", "calibri")
# # numbers = (12, 5, 3, 3)
# # tv_chanel = ("netflix", "prime", "disney")
# # ingredients = ("flour", "milk", "salt")


# # house = {
# #     "name": "2 bed",
# #     "location": "lagos",
# #     "room":[
# #         {"name": "Bedroom", "items found": [
# #             "lamp", "flower", "keys", "condom"
# #             ]
# #         },
# #         {"name": "kitchen", "items found": [
# #             "knife", "cups", "glass"
# #             ]
# #          }
# #     ]
# # }

# # house ={"name":"2 bed", "location",:"lagos",
# #         "room":["Bedroom":["lamp", "flower", "keys", "condom"]
# #         ],
# #         "room":["kitchen":["knife", "cups", "glass"]
# #         ]

# # }
# # different ways of writing dictionaires
# # person = {"name": "onyi", "age": 878, "city": "London"}  example 1
# # print(person.keys())
# # print(person.values())

# # person = {
# #     "name": "onyi",           example 2
# #     "age": 2,
# #     "city": "London"
# # }

# # person = {}
# # person["name"] = "onyi"       example 3
# # person["age"] = 2
# # person["city"] = "London"
# # list
# # fruits = ["apple", "banana", "orange"]
# # fruits = [
# #     "apple",
# #     "banana",
# #     "orange"
# # ]
# # fruits = []
# # fruits.append("apple")
# # fruits.append("banana")
# # fruits.append("orange")

# # fruits[0] = "pineapple"
# # fruits.append("pineapple")
# # fruits.remove("banana")
# # fruits.insert(0,"pineapple")
# # fruits.sort()
# # fruits.reverse()
# # fruits.clear()

# # print() function
# # add()
# # object.add()
# # print.__eq__()
# # object[0]()
# # print.object.object()
# # sub()
# # object()
# # str()
# # my_list=[print]
# # my_list[0]("the world is beautiful")
# # my_list # list
# # my_list[0] # index 0
# # print 
# # print("the world is beautiful")

# # my_arr = [3, str]

# # my_arr[0] += 1
# # print(my_arr[1](my_arr[0]))



# # my_arr[1] #index 1
# # [3,str] #inside the list
# # [0,1] #actual position of the above
# # str # the value of index 1
# # str(4)
# # print(str(4))

# # my_arr = [
# #     3, 
# #     str, 
# #     {"function": print, "add_value": 5}
# # ]

# # my_arr[0] += my_arr[2]["add_value"] #changed the index from 3 to 2 as the 3 was incorrect
# # my_arr[2]["function"](my_arr[1](my_arr[0]))

# # my_arr[2]["add_value"] #breaking it down to sessions
# # my_arr[2]
# # {"function": print, "add_value": 5} # this is the value for index 2
# # {...} ["add_value"]
# # 5
# # my_arr[0] +=5

# # my_arr[2]["function"]
# # my_arr[2]
# # print(8)



# # my_arr # list
# # 3 # index [0]
# # str # function used in converting to a string
# # {"function": print, "add_value": 5} # a dictionary with two keys

# # my_arr[0]  # index 0 = 3
# # my_arr[3] #index 3 = ERROR! There is no index 3 (only 0, 1, 2)

# # def my_result ():
# #     print(8)
# # my_result()
    
# # def       # no limit on defining functions and read the book he sends to you
# #           # functions are blocks of code that do certain things for you

# # def greet():
# #     print("Hello, Onyi!")

# # # Call the function
# # greet() 

# # def greet_person(name):   # automate the boring stuff
# #     print("Hello", (name))

# # greet_person("Alice")  
# # greet_person("Bob")    
          

# # def add_numbers(a, b):   #youtube
# #     result = a + b
# #     return result

# # sum = add_numbers(5, 3)
# # print(sum)  



# # def record_sale(product:dict, quantity_sold: int = 5):
# #     product["quantity"] -= quantity_sold 
# #     return product

# # milk = {"name": "milk", "quantity": 40, "price": 1.20}

# # print("Before sale:", milk["quantity"])

# # record_sale(quantity_sold = 6, product = milk)
# # milk = record_sale(milk)
# # milk = record_sale(milk, 3)
# # milk = record_sale(milk, 10)


# # print("After sale:", milk["quantity"])


# # import random as rd                 # recreate again

# # def Style(stype:int= 0):
# #     if stype == 1:
# #         return "\033[31m" # Red
# #     elif stype == 2:
# #         return "\033[32m" # Green
# #     else:
# #         return "\033[0m" # Reset

# # print("\n")
# # print("Number Guessing game".center(100, "="))
# # print("\nTry and beat the game with as little guesses as possible")
# # print("Guess from 1 - 100\n")

# # guess_number = 0
# # guess = rd.randint(1, 100)
# # number_of_guesses = 0
# # while True:
# #     output: str = input("Your Guess: ")
# #     if output == "xx": 
# #         break

# #     if not output.isdigit():
# #         print(f"{Style(1)}Error; this is not a digit; ({output}){Style(0)}")
# #         continue
    
# #     guess_number = int(output)

# #     if guess == guess_number:
# #         break

# #     if guess > guess_number:
# #         print("Guess higher")
# #     else:
# #         print("Guess lower")
# #     number_of_guesses += 1

# # print(f"{Style(2)}Congrats!!! You guessed the \
# # number in {number_of_guesses} guesses.{Style(0)}")
# # print("\n\n")

# # import fsutil
# # fsutil.create_file("love.txt", "perfect life")

# import random as rd

# print("GUESS THE NUMBER")
# print("Choose number between 1 and 200\n")

# secret_number = rd.randint(1, 50)
# number_of_tries = 2

# while True:
#     guess = input("Your guess: ")
    
#     if guess == "stop":
#         print("Goodbye! try again next time.")
#         break
    
#     if not guess.isdigit():
#         print("Enter a number!")
#         continue
    
#     guess = int(guess)
#     number_of_tries = number_of_tries + 1
    
#     if guess == secret_number:
#         print(f"YOU WIN you sexy person!!! in {number_of_tries} number_of_tries!")
#         break
#     elif guess < secret_number:
#         print("Higher baby!")
#     else:
#         print("Lower hun!")

# Ask gpt what is project and apps
# revision on what was learned today

# 13th friday 2026
# Research on status Code
# search for examples of json

# my_lists= [0,1,2,3,]

# Core drill: “Create the Pharmacy Structure”
# Scenario from PRD:
#  The system has inventory, sales, and users. They must not be mixed.
# Exercise:
# Create a Django project
# Create three apps:

# inventory
# sales
# users
# Register the apps properly


# create 3 projects and two apps in each of those projects
# play around with module
# look at the things with the eye moduling
# model 5 things

# def outer_func():
#     msg = 'Hello there!'

#     def inner_func():
#         print(msg)

# print(msg)
# number = 375
# print(3+number)
# print(3+number)
# print(3+number)
# print(3+number)

# def addthe(a,b,c,d,e):
#     print(a+b+c+d+e)
# addthe(1,2,3,2,4)

# Exercise:
# Create a function called record_sale
# It should:

# Accept product dictionary
# Accept quantity sold
# Reduce stock
# Return updated product

# Optional extension:
# Add sale amount to daily total
# What this drill proves:
# You can reuse logic
# You can pass data in and out
# You are ready for Django views
# This is the bridge into real backend work.

# product={'name': 'pad', 'stock': 90, 'price': 23}

# def record_sale(the_product,quantity_sold):
#     the_product['stock']-= quantity_sold
#     return the_product
# print(record_sale(product,50))

# if 3:
#     print('yes')
# if 0:
#     print('yesssssss')
# if "yes":
#     print('yes')
# if '':
#     print('no')

# # Assignment
# # recreate if,elif statement with Code
# age = 20
# if age < 20:
#     print('below age required')

# while True:
#     print(5)
#     break

# def greet():              ← No indent (function starts)
#     print("Hello")                     inside function
#     print("Welcome")                   inside function

# age = 18

# if age >= 18:
#     print("You can vote")             inside 
#     print("Register now")             inside function
# print("Thank you")                   not in function will print regardless
boob_size = print()
boob_size('i love boobies')

