# import time

# call method for this is @decoratortimer()
# def decoratortimer(decimalplaces=3):
#     def decoratorfunction(f):
#         def wrap(*args, **kwargs):
#             if type(decimalplaces) != int:
#                 raise ValueError('Only integers are allowed for decimalplaces')

#             time1 = time.monotonic()
#             result = f(*args, **kwargs)
#             time2 = time.monotonic()
#             print('{:s} function took {:.{}f} ms'.format(f.__name__, ((time2-time1)*1000.0), decimalplaces ))
#             return result
#         return wrap
#     return decoratorfunction

# call method for this is @decoratortimer OR @decoratortimer(decimalplaces = *args)
from functools import wraps, partial
import time

def decoratortimer(func = None, decimalplaces = 3):
    if func is None:
        return partial(decoratortimer, decimalplaces= decimalplaces)
    @wraps(func)
    def wrapper(*args,**kwargs):
        if type(decimalplaces) != int:
            raise ValueError('Only integers are allowed for decimalplaces')

        time1 = time.monotonic()
        result = func(*args, **kwargs)
        time2 = time.monotonic()
        print('{:s} function took {:.{}f} ms'.format(func.__name__, ((time2-time1)*1000.0), decimalplaces ))
        return result
    return wrapper
    


