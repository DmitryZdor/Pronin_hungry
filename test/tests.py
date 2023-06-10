import unittest
from git_link import git_link
from  lambda_map import lambda_map
from strange_dict import strange_dict
from cls_text import TextFunctions



class GitLinkFunc(unittest.TestCase):
    def test_link(self):
        self.assertEqual(*git_link(['f']), 'Ссылка f имеет неверный формат')
        self.assertEqual(*git_link(['https://github.com/DmitryZdor/news_for_test']), 'news_for_test')
        self.assertEqual(git_link([]), 'Нет данных')


class LambdaMap(unittest.TestCase):
    def test_lambda(self):
        self.assertEqual(list(lambda_map([4, 'a', '',34 , 0])), [16, 'abc_a_cba', 'abc__cba',1156 ,0])

class StrDict(unittest.TestCase):
    def test_dict(self):
        self.assertEqual(strange_dict([1, 2, 3], ['A', 'B', 'C']), 'Списки равны')
        self.assertEqual(strange_dict(
            [5, 3, 2, 1, 4, 6, 9], ['E', 'C', 'B', 'A', 'D']), {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
        )

class TextCls(unittest.TestCase):
    pass



if __name__ == '__main__':
    unittest.main()
