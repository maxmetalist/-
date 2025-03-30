from functools import wraps


def log(filename=None):
    """Декоратор, логирующий выполнение функций"""

    def wrapper(function):
        """Обёртка для функции"""

        @wraps(function)
        def inner(*args, **kwargs):
            """собственно сама функция. Ниже блок записи лога"""

            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{function.__name__} ok. Res: {function(*args, **kwargs)}")
                else:
                    print(f"{function.__name__} ok. Res: {function(*args, **kwargs)}")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}")

        return inner

    return wrapper


# @log()
# def my_function(x, y):
#     return x / y
#
# my_function(1, 2)
