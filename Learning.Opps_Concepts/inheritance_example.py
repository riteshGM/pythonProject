class Human:
    name = ""
    age = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age


class Profession(Human):
    occupation = ""

    # Need to Initialize Parent Variables Explicitly
    def __init__(self, occupation, age, name):
        self.occupation = occupation
        self.age = age
        self.name = name

    def getoccupation(self):
        return self.occupation


# humanObj = Human("Ritesh", "25")
# print(humanObj.getage())
# print(humanObj.getname())

occupationObj = Profession("Programmer", "25", "Ritesh")
print(occupationObj.getname())
print(occupationObj.getage())
print(occupationObj.getoccupation())


