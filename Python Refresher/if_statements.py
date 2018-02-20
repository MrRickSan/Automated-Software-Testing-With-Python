# should_continue = True
# if should_continue:
#     print('Hello')

# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")

# if person in known_people:
#     print("You know {}!".format(person))
# else:
    # print("You don't know {}!".format(person))

# if person not in known_people:
#     print("You don't know this person!")

## Exercise

def who_do_you_know():
    #Ask the user for a list of people they know
    #Split the string into a list
    #Return that list
    list_of_people = []
    users_wants_to_input = True
    while users_wants_to_input == True:
        var1 = input("Enter the name and press [Enter] of persons that you know (Write 'Exit' if you want to stop): ")
        if var1 == "Exit":
            users_wants_to_input == False
            break
        else:
            list_of_people.append(var1)
    print(list_of_people)
    return list_of_people

def who_do_you_know_with_Split():
    #Ask the user for a list of people they know
    #Split the string into a list
    #Return that list
    people = input("Enter the names of persons that you know, separated by commas: ")
    normalised_people = [person.strip().lower() for person in people.split(",")]
    return normalised_people
    # list_whithout_spaces = []
    # for person in list_of_people:
    #     list_whithout_spaces.append(person.strip())
    # return list_whithout_spaces

def ask_user():
    #Ask the user for their name
    #See if their name is in the list of people they know
    #Print out that they know the person
    username = input("Write your name and hit [Enter]: ")
    if username in who_do_you_know_with_Split():
        print("They know {}!".format(username))
    else:
        print("They don't know {}!".format(username))
    # for name in list:
    #     if username == name:
    #         print("They know {}!".format(username))
    #         return
    # print("They don't know {}!".format(username))


# who_do_you_know()
# list = who_do_you_know_with_Split()
ask_user()
