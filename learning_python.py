# my_list=[3,4,7,8,20]
# total=0
# for items in my_list:
#     total+=items
#     print(total, items)

# collection = single "variable" used to store multiple values
# list=[] order and changeable. duplicates ok
# set={} unordered and immutable, but add/remove ok. No duplicates
# tuple = () ordered and unchangeable. duplicates ok. faster

# fruits = ["apple", "banana", "orange", "kiwi"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# # print(fruits[0])
# for fruit in fruits:
#     print(fruits)
# # fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("banana")
# fruits.insert(0,"pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index[0])
# # SET
# fruits = {"apple", "banana", "orange", "kiwi"} 
# fruits.add("pineapple")
# fruits.remove("pineapple")
# # TUPLE
# fruits = ("apple", "banana", "orange", "kiwi")

# Variable = a resuable container for storing value
#
#           a variable behaves as if it were the value it contains
#age = 39
# print(age) if you are printing a variable you dont have to put it in quotes
# print("you are " +  str(age) +  " years old")

# create a variable condition
# cold or hot variable, check for is hot is it cold and dependant on whether it is cold or not wear a hoodie or bum shorts

# weather = "cold"
# # outcome ={"cold": "wear sweater", "hot":"wear bum short"}
# # outcome[weather]
# # print(outcome[weather])

# if weather == "cold":
#     print("wear sweater")
#     print("also carry a jacket")
# elif weather == "hot":
#     print("wear bum short")
# else: 
#     print("wrong weather type")

# def hello():
#     # Prints three greetings
#     print('Good morning!')

# def say_hello_to(name):
#     # Prints three greetings to the name provided
#     print('Good morning, ' + name)
#     print('Good afternoon, ' + name)
#     print('Good evening, ' + name)

# say_hello_to('Alice')
# say_hello_to('Bob')

# def get_answer(answer_number):
#     # Returns a fortune answer based on what int answer_number is, 1 to 9
#     if answer_number == 1:
#         return 'It is certain'
#     elif answer_number == 2:
#         return 'It is decidedly so'
#     elif answer_number == 3:
#         return 'Yes'
#     elif answer_number == 4:
#         return 'Reply hazy try again'
#     elif answer_number == 5:
#         return 'Ask again later'
#     elif answer_number == 6:
#         return 'Concentrate and ask again'
#     elif answer_number == 7:
#         return 'My reply is no'
#     elif answer_number == 8:
#         return 'Outlook not so good'
#     elif answer_number == 9:
#         return 'Very doubtful'

# print('Ask a yes or no question:')
# input('>')
# r = random.randint(1, 9)
# fortune = get_answer(r)
# print(fortune)

# print('My favorite colors are', 'blue', 'green', 'red')

# my_str = "hello onyi"
# my_spilt_str = my_str.replace("hello", "yo")
# print(my_spilt_str)

# my_str = 'hello world'

# replaced_my_str = my_str.replace('hello', 'hi')
# print(replaced_my_str) 

# my_str = 'hello world'

# starts_with_hello = my_str.startswith('hello')
# print(starts_with_hello) 

my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1
print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) 

product = 65
product *= 7

print(product)

greet = 'Hello'
greet += ' World'

print(greet)