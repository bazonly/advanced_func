from random import randint
import time
from math import sqrt, ceil, floor

def create_list(len_list):
    list = []
    for i in range(len_list):
        list.append(randint(1, 10))
    return list

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Function: ', func.__name__, 'took: ', end-start, 'seconds run')
        return result
    return wrapper


@time_it
def sqrt_list(lst: list, is_floor=True):
    time.sleep(2)
    new_lst = []
    for item in lst:
        if is_floor:
            item = int(
                floor(
                    sqrt(item)
                )
            )
        else:
            item = int(
                ceil(
                    sqrt(item)
                )
            )
        new_lst.append(item)
    return new_lst


lst = create_list(randint(5, 20))
print(lst)
new_lst = sqrt_list(lst, False)
print(new_lst)
