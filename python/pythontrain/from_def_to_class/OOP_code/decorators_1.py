def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class MyClass:
    @log_call          # <-- свой декоратор
    def say_hello(self):
        print("Hello!")

test = MyClass()
test.say_hello()