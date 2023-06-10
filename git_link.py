def git_link(links):
    """ Функция принимает в качестве аргумента набор ссылок и возвращает название проекта. """
    if links:
        res = list(link.split('/')[4].split('.')[0] if link.startswith('https://github.com')
                else f'Ссылка {link} имеет неверный формат' for link in links)
        return res
    else:
        return 'Нет данных'
