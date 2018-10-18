import collections
import time
import timeit
def tester(*args):
    print(*args)



def usual_dict(dict_data):
    newdata = {}
    for k, v in dict_data:
        if k in newdata:
            newdata[k].append(v)
        else:
            newdata[k] = [v]
    return newdata

def setdefault_dict(dict_data):
    newdata = {}
    for k, v in dict_data:
        newdata.setdefault(k, []).append(v)
    return newdata

def test_setdef(module_name='this module'):
    dict_data = (('key1', 'value1'), ('key1', 'value2'), ('key2', 'value3'), ('key2', 'value4'), ('key2', 'value5'))
    print(usual_dict(dict_data))
    print(setdefault_dict(dict_data))
    print()
    return setdefault_dict(dict_data)



def square ( x ):
    return x ** 2

def f ( x ):
    return x * x

def try_f ( f ):
    return f ( 3 )

print(f ( 3 ) == square ( 3 ))