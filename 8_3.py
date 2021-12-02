'''Третье задание'''

from functools import wraps


def type_logger(func):

    def wrapper(*args):
        for i in args:
            print(f'{func.__name__}({i}: {type(i)})', end=', ')
        return func(*args)

    return wrapper

@type_logger
def calc_cube(*args):
    return args

a = calc_cube(5.4, 23, 'hi', ['world'])

print(a)

