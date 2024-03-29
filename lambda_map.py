def lambda_map(lst):
    """Функция принимает список элементов (состоящий из строк и цифр),
    возвращает новый список, с условием - если элемент списка был строкой, в начало строки нужно добавить текст "abc_",
    в конец строки - "_cba". Если элемент был int - то его значение нужно возвести в квадрат."""
    txt = 'abc_'

    return list(map(lambda x: x * x if isinstance(x, int) else txt + x + txt[::-1], lst))
