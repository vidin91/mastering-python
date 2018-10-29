# Classes

# Basic example
class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def sayhello(self):
        return 'Hi! I\'m ' + self.name + self.lastname


p1 = Person('Milos', 'Milenovic')
print(p1)
# >>> <__main__.Person object at 0x0030E950>

Person.__str__ = lambda x: 'Hello World!'
print(p1)
# >>> Hello World!

attr = p1.__getattribute__('sayhello')
print(attr)
# >>> <bound method Person.sayhello of <__main__.Person object at 0x0030E950>>


# classes can contain statements
glob_var = True
class T:
    if glob_var:
        def saysomething(self):
            print('something ;)')


obj = T()
obj.saysomething()
# >>> something ;)

