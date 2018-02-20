a = 5
b = 10
my_variable = 56
any_variable_name = 10

string_variable = "hello"
single_quotes = 'string can have single quotes'

# print(my_variable)
# print(string_variable)

def my_print_method(my_argument):
    print(my_argument)

# my_print_method(single_quotes)

def my_multiply_method(number_one, number_two):
    return number_one * number_two

result = my_multiply_method(5, 3)
# my_print_method(result)

my_print_method(my_multiply_method(5, 3))
