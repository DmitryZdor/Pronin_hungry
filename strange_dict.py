def strange_dict(lst1, lst2):
    """Реализовать функцию, принимающую два списка и возвращающую словарь, упорядоченный по ключам """
    return dict(sorted(zip((lst1), lst2))) if len(lst1) != len(lst2) else 'Списки равны'


