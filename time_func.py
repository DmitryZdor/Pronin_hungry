import time
from cls_text import TextFunctions


def time_func(func):
    """Декоратор замеряет скорость выполнения функции."""

    def wrapper(*args, **kwargs):
        beg_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        time_res = end_time - beg_time
        print(f'Функция "{func.__name__}": выполняется {time_res} с.')
        return result
    wrapper.__name__ = func.__name__
    return wrapper


def for_all_methods(decorator):
    """" Функция проводит декоратор по всем методам класса"""
    def decorate(cls):
        for attr in cls.__bases__[0].__dict__:
            if callable(getattr(cls, attr)) and not attr.startswith('__'):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate


@for_all_methods(time_func)
class TextFuncDecor(TextFunctions):
    pass
