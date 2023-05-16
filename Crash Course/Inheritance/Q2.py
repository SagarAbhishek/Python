class Animals:
    @staticmethod
    def eat():
        print('eating')
class pets(Animals):
    color='white'
class dog(pets):
    @staticmethod
    def bark():
        print('dog is barking')

d=dog()
d.bark()
d.eat()