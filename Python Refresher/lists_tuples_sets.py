my_variable = 'hello'

grades = [77, 80, 90]
tupple_grades = (77, 80, 90) #immutable
set_grades = {77, 80, 90, 100, 100} #unique & unordered

grades.append(108)

print(sum(grades) / len(grades))
print(set_grades)
print(tupple_grades)

tupple_grades = tupple_grades + (100,)
print(tupple_grades)

set_grades.add(60)
print(set_grades)

your_lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}

print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
print(your_lottery_numbers.difference(winning_numbers))