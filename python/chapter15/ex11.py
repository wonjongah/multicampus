class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


kim = Human("김상형", 29)
sang = Human("김상형", 29)
moon = Human("문종민", 44)

print(kim == sang)
print(kim == moon)