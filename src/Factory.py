# Trong Factory Pattern,
# chúng ta tạo đối tượng mà không để lộ logic tạo đối tượng ở phía người dùng
# và tham chiếu đến đối tượng mới được tạo ra bằng cách sử dụng một interface chung.
#
# Factory Pattern được sử dụng khi có một class cha (super-class)
# với nhiều class con (sub-class), dựa trên đầu vào và phải trả về 1 trong những class con đó.


# Animal interface
class IAnimal(object):
    def get_voice(self):
        pass


# Dog
class Dog(IAnimal):
    def get_voice(self):
        print("Woof Woof")


# Cat
class Cat(IAnimal):
    def get_voice(self):
        print("Meow meow")


# Monkey
class Monkey(IAnimal):
    def get_voice(self):
        print("Minh keu khec khec")


# Animal Factory
class AnimalFactory(object):
    @staticmethod
    def create_animal(animal_name):
        if animal_name == "Dog":
            return Dog()
        elif animal_name == "Cat":
            return Cat()
        elif animal_name == "Monkey":
            return Monkey()
        print("Invalid Name")
        return -1


# Client
while True:
    choice = input("Enter animal Name: ")
    s = choice.capitalize()
    animal = AnimalFactory.create_animal(s)
    animal.get_voice()


