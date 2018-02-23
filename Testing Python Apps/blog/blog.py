class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        pass

    def create_post(self, title, content):
        self.posts.append({'title': title, 'content': content,})

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': self.posts,
        }