# data types - overview

"""
    Numbers
"""
def numbersTest():
    print(int)
    # >>> <class 'int'>

    print(type(10))
    # >>> <class 'int'>

    print(0xf)
    # >>> 15

    print(type(4.2))
    # >>> <class 'float'>


"""
    Strings
"""
def stringsTest():
    ref = str
    print(ref)
    # >>> <class 'str'>

    name = 'Milos'
    lastName = 'Milenovic'
    fullName = name + " " + lastName
    print('User' + ''': ''' + fullName)
    # >>> User: Milos Milenovic

    print('''
    Milos
    milenovic
    ''')
    # >>> Milos
    #   milenovic
    print(name.__len__())
    # >>> 5

    print(len(name))
    # >>> 5

    print('belgrade'.capitalize())
    # >>> Belgrade

    for char in 'city':
        print(char)
    # >>> c
    #     i
    #     t
    #     y

    testSting = 'some RanDom senTence'
    cnt = 0
    for i in range(0, len(testSting)):
        if testSting[i].isupper():
            cnt += 1
    print(cnt)

    print(testSting.find('sen'))
    # >>> 12

    words = testSting.split()
    print(words)
    # >>> ['some', 'RanDom', 'senTence']


"""
    Lists
"""
def listsTest():
    randomList = [10, "Milos", {}, True]
    print(randomList)
    # >>> [10, 'Milos', {}, True]

    print(type(randomList))
    # >>> <class 'list'>

    print(randomList.index({}))
    # >>> 2 (This is weird!!!!!!!!!!!!!!!!!!!)

    randomList.append(22)
    print(randomList)
    # >>> [10, 'Milos', {}, True, 22]

    users = ["Milos", 'Janko', "Stanko"]
    randomList.extend(users)
    print(randomList)
    # >>> [10, 'Milos', {}, True, 22, 'Milos', 'Janko', 'Stanko']

    randomList.remove("Janko")
    print(randomList)
    # >>> [10, 'Milos', {}, True, 22, 'Milos', 'Stanko']

    numbers = [1, 2, 3]
    numbers2 = list(numbers)  # argument is iterable
    ref = numbers
    print(numbers == numbers2)
    print(numbers is numbers2)
    print(numbers is ref)
    # >>> True
    #     False
    #     True

"""
    Tuples
"""
def tuplesTest():
    numbers = (1, 2, 3)
    t = tuple(numbers + numbers)
    print(t)
    # >>> (1, 2, 3, 1, 2, 3)

    print(type(t))
    # >>> <class 'tuple'>

    n = (2)  # This is not tuple
    print(n)
    # >>> 2

    n = (2,)  # This is tuple with single element
    print(n)
    # >>> (2,)


"""
    Dictionaries
"""
def dictionariesTest():
    # user = {name: 'Milos'} - Error: Unresolved reference 'name'
    user = {'name': 'Milos', 'lastName': 'Milenovic', 'age': 27}
    print(user)
    # >>> {'name': 'Milos', 'lastName': 'Milenovic', 'age': 27}

    print(type(user))
    # >>> <class 'dist'>

    # print(user.name) - AttributeError: 'dict' object has no attribute 'name'

    print(user['name'])
    # >>> Milos

    t = {10: 20, 'uno': 'duo'}
    print(t.keys())
    # >>> dict_keys([10, 'uno'])

    print(t.items())
    # >>> dict_items([(10, 20), ('uno', 'duo')])

    print(t.values())
    # >>> dict_values([20, 'duo'])

    t2 = t.copy()
    print(t2 == t)
    print(t2 is t)
    # >>> True
    #     False


# numbersTest()
# stringsTest()
# listsTest()
# tuplesTest()
# dictionariesTest()
