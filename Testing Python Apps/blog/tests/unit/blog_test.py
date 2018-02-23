from unittest import  TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

        # could be made this way too
        #self.assertEqual(0, len(b.posts))

    def test_repr(self):
        pass

    def test_create_post(self):
        b = Blog.create_post('Title', 'Content')
        expected = {'title': 'Title', 'content': 'Content',}

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Title', 'Content')

        expected = {'title': 'Test', 'author': 'Test Author', 'posts': '[ {"title": Title, "content": "Content",} ]'}

        self.assertDictEqual(expected, b.json())