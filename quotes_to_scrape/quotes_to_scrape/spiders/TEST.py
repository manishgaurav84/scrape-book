def abc():

    print('abc')
    yield 2
    print('xyz')
    yield 3


if __name__=='__main__':
    y = abc()

    print(y.__next__())
    print(y.__next__())