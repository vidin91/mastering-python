class BaseClass:
    pass


class User(BaseClass):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


user = User('Milos', 'Milenovic')

print(user.__dict__)  # dictionary
# >>> {'name': 'Milos', 'lastname': 'Milenovic'}

print(User.__dict__)
# >>> {'__module__': '__main__', '__init__': <function User.__init__ at 0x011D3A98>....

print(type(User))
# >>> <class 'type'>

print(user.__class__)
# >>> <class '__main__.User'>

print(type)
# >>> <class 'type'>

print(type(user) is User)
# >>> True

print(type(user) is BaseClass)
# >>> False

print(isinstance(user, BaseClass))
# >>> True

print(User.__class__)
# >>> <class 'type'>

print(User.__bases__)
# >>> (<class '__main__.BaseClass'>,)

"""
    Name mangling:
    “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python
    By convention: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API
    Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore)
    is textually replaced with _classname__spam
    Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls
    Like private methods in c++ - not visible to child classes.
"""

class A:
    def __gettext(self):
        return 'class A'

obj = A()
# obj.__gettext()  - AttributeError: 'A' object has no attribute '__gettext'

print(obj._A__gettext())
# >>> class A

### DESCRIPTORS - TODO!