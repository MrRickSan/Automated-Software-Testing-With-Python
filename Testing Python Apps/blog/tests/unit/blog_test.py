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
        b = Blog('Title', 'Test Author')
        b2 = Blog('My Day', 'Rolf')

        self.assertEqual(b.__repr__(), ('{} by {} (0 posts)'.format(b.title, b.author)))
        self.assertEqual(b2.__repr__(), ('{} by {} (0 posts)'.format(b2.title, b2.author)))

    def test_repr_multiple_posts(self):
        b = Blog('Title', 'Test Author')
        b.posts = ['test']

        b2 = Blog('My Day', 'Rolf')
        b2.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), ('{} by {} (1 post)'.format(b.title, b.author)))
        self.assertEqual(b2.__repr__(), ('{} by {} (2 posts)'.format(b2.title, b2.author)))