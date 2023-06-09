def git_link(links):
    """ Функция принимает в качестве аргумента набор ссылок и возвращает название проекта. """
    print(*(link.split('/')[4].split('.')[0] if link.startswith('https://github.com')
            else f'Ссылка {link} имеет неверный формат' for link in links), sep='\n')

# можно было не в одну строку, но так мне больше понравилось

# тестовые данные
git_link(['https://github.com/miguelgrinberg/Flask-SocketIO', 'https://github.com/miguelgrinberg/Flask-SocketIO.git',
         'https://github.com/DmitryZdor/news_for_test', 'https://gothub/DmitryZdor/news_for_test'])
