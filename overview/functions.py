# testing scopes and namespaces
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    # >>> After local assignment: test spam

    do_nonlocal()
    print("After nonlocal assignment:", spam)
    # >>> After nonlocal assignment: nonlocal spam

    do_global()
    print("After global assignment:", spam)
    # >>> After global assignment: nonlocal spam


scope_test()
print("In global scope:", spam)
# >>> In global scope: global spam


def t(x):
    if x:
        val = 100
    print(val)  # if x is falsy: UnboundLocalError: local variable 'val' referenced before assignment
# => scopes are determened by function definitions (not statement blocks, like in JS)


glob_var = 'Belgrade'
class T:
    if glob_var:
        def saysomething(self):
            print('something ;)')


obj = T()
obj.saysomething()