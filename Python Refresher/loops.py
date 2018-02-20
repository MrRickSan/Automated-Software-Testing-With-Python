var1 = "hello, world"

for i in var1: #iterables are strings, lists, sets, tuples and more
    print(i)

my_list = [1,3,5,7,9]

for i in my_list:
    print(i ** 2)

user_wants_number = True
while user_wants_number == True:
    print(10)
    # user_wants_number = False
    user_input = input("Should we print again? (y/n)")
    if user_input == 'n':
        user_wants_number = False