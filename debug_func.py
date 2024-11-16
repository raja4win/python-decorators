


def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ','.join(str(arg) for arg in args)
        kwargs_value = ','.join(f"{k}: {v}" for k,v in kwargs.items())
        print(f"calling {func.__name__} with args: {args_value}")
        print(f"calling {func.__name__} with kwargs: {kwargs_value}")

        func(*args, **kwargs)
        # print("inside wrapper")
    return wrapper

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


greet("indranil", greeting="Namaskar")

greet("Pompi", greeting="Morning")
