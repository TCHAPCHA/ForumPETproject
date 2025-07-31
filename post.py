class Post:
    id = -1
    def __init__(self, id, title, content, author, likes=0):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.likes = likes