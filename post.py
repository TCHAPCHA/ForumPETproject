class Post:
    def __init__(self, ident: int, title: str, content: str, author: str, likes: int=0):
        """Initialize a post."""
        self.id = ident
        self.title = title
        self.content = content
        self.author = author
        self.likes = likes

    get_id = lambda self: self.id # Get ID of post
    get_author = lambda self: self.author # Get post's author
    get_title = lambda self: self.title # Get the title of the post
    get_content = lambda self: self.content # Get the content of the post
    get_likes = lambda self: self.likes # Get likes quantity of the post