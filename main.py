from git_link import git_link
from lambda_map import lambda_map
from strange_dict import strange_dict
from cls_text import TextFunctions
from time_func import TextFuncDecor
from requests_100 import client_blacksheep, report_time, URL, TIMES
import asyncio

functions = {'git_link': [['https://github.com/miguelgrinberg/Flask-SocketIO',
                           'https://github.com/miguelgrinberg/Flask-SocketIO.git',
                           'https://github.com/DmitryZdor/news_for_test',
                           'https://gothub/DmitryZdor/news_for_test'], [], ['f'],
                          ['https://github.com/DmitryZdor/news_for_test']],

             'lambda_map': [['Функция', 44, 658, 'принимает', 54, 'список', 'элементов', '(состоящий из строк и цифр),',
                             'возвращает', 4, 'новый список,', 34578, '23345656']],

             'strange_dict':
                 [
                     (list(reversed('ABCDEFGHIJKLMNOPQRSTUVWXYZ')), list('987654321')
                      ), ]
             }
if __name__ == '__main__':
    for func, data in functions.items():
        for el in data:
            print(f'Название функции {func}')
            print(f'назначение: {eval(func).__doc__}')
            print(f'тестовые данные: {el}')
            if func == 'strange_dict':
                print('Результат :', eval(f'{func}(*{el})'))
            else:
                print('Результат :', eval(f'{func}({el})'))
            print()

    print('Проверка методов класса принимающего на вход текст')
    data = ('Написаться Ссасс, принимающий: на входаааааааааааа ПотОп... (Один Метод), метоД,  должен выводить.. "в",'
            ' меТод- самое$ длинное слово в')
    print('Данные:', data)
    a = TextFunctions(text=data)
    list_of_methods = ['longest_word', 'all_palindromes', 'symbols_quantity', 'often_word']
    for attr in list_of_methods:
        print(f'Результат функции: {getattr(a, attr).__name__}, которая {getattr(a, attr).__doc__}'
              f'\n {getattr(a, attr)()}')
    print('---------Демонстрация работы декоратора показывающего время выполнения метода в классе------------------'
          '------------------------------------------------')

    b = TextFuncDecor(text=data)
    for attr in list_of_methods:
        print(f'Результат функции: {getattr(b, attr).__name__}  -  {getattr(b, attr)()}')

    print('------Функция, которая замеряет время на исполнение 100 запросов к адресу  http://httpbin.org/delay/3  '
          '------------------------------------------------')

    loop = asyncio.get_event_loop()
    with report_time("blacksheep"):
        loop.run_until_complete(
            asyncio.gather(*[client_blacksheep(URL) for i in range(TIMES)]))
