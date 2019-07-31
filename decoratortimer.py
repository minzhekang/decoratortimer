import time

def decoratortimer(decimalplaces=3):
    def decoratorfunction(f):
        def wrap(*args, **kwargs):
            if type(decimalplaces) != int:
                raise ValueError('Only integers are allowed for decimalplaces')

            time1 = time.monotonic()
            result = f(*args, **kwargs)
            time2 = time.monotonic()
            print('{:s} function took {:.{}f} ms'.format(f.__name__, ((time2-time1)*1000.0), decimalplaces ))
            return result
        return wrap
    return decoratorfunction
