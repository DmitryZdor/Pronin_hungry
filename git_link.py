def git_link(links):
    """ Функция принимает в качестве аргумента набор ссылок и возвращает название проекта. """
    if links:
        res = list(link.split('/')[4].split('.')[0] if link.startswith('https://github.com')
                else f'Ссылка {link} имеет неверный формат' for link in links)
        return res
    else:
        return 'Нет данных'
# можно было не в одну строку, но так мне больше понравилось

# тестовые данные
if __name__ == '__main__':


    print(git_link(['https://github.com/miguelgrinberg/Flask-SocketIO', 'https://github.com/miguelgrinberg/Flask-SocketIO.git',
             'https://github.com/DmitryZdor/news_for_test', 'https://gothub/DmitryZdor/news_for_test']))

    print(git_link([]))

    print(git_link(['f']))

    git_link(['https://github.com/DmitryZdor/news_for_test'])