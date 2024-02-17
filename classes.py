class Person:
    name = ""
    age  = 0

    def femPers(self):
        print("She was the top student in last semester exams.")

person1 = Person()
person2 = Person()

person1.name = "Hellen"
person1.age = 16

person2.name = "Henry"
person2.age = 18

print(person1.name, person2.name)

print(person2.name + " is eligible to vote.")

person1.femPers()