lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (13, 45, 66, 23, 22)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)
    
    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_two = LotteryPlayer("John")

print(player_one.name)
print(player_one.numbers)
print(player_one.total())

print(player_one.name == player_two.name)
print(player_one.numbers == player_two.numbers)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    def go_to_school(self):
        print("{} is going to {}".format(self.name,self.school))
    
    @classmethod
    def go_to_school_without_self_with_cls(cls):
        print("I'm going to {}".format(cls))

    #all the methods will share the same data
    @staticmethod
    def go_to_school_without_self_and_cls():
        print("I'm going to school")


anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")

anna.marks.append(56)
anna.marks.append(71)

print(anna.average())
anna.go_to_school()
rolf.go_to_school()
anna.go_to_school_without_self_with_cls()
Student.go_to_school_without_self_and_cls()