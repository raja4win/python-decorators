import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        print(cache_value)
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args]=result
        return result
    return wrapper

@cache
def long_running_func(a,b):
    time.sleep(4)
    return a+b


print(f"value returned is {long_running_func(2,3)}")
print(f"value returned is {long_running_func(2,3)}")
print(f"value returned is {long_running_func(2,3)}")
print(f"value returned is {long_running_func(4,3)}")
print(f"value returned is {long_running_func(2,3)}")
print(f"value returned is {long_running_func(6,3)}")
print(f"value returned is {long_running_func(4,3)}")
print(f"value returned is {long_running_func(6,3)}")

    