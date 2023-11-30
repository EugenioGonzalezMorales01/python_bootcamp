def loggin_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        func(args[0], args[1], args[2])

    return wrapper


@loggin_decorator
def sum(*args):
    total = 0
    for arg in args:
        total += arg
    print(f"it returned: {total}")


sum(1, 2, 3)
