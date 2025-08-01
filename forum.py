from user import User, Admin
from post import Post

class Forum:
    users = []
    def __init__(self, forum_name: str):
        """Initialize a new forum"""
        self.id = 0
        self.posts = []
        self.likes = []
        self.forum_name = forum_name

    def create_post(self, title: str, content: str, author: str):
        """Create a new post"""
        for user in self.users:
            if user.username == author:
                post = Post(self.id, title, content, author)
                self.id += 1
                self.posts.append(post)
                print(f"Post created with id '{post.id}'")
                return post
        return None

    def create_user(self, username: str, email: str):
        """Create a new user"""
        for user in self.users:
            if user.username == username or user.email == email:
                print("User already exists")
                return None
        user = User(username, email)
        self.users.append(user)
        print(f"User created with username '{user.username}'")
        return user

    def create_admin(self, username: str, email: str):
        """Create a new admin"""
        for user in self.users:
            if user.username == username or user.email == email:
                print("User already exists")
                return None
            if user.username == username or user.email == email:
                print("User already exists")
                return None
        admin = Admin(username, email)
        self.users.append(admin)
        print(f"Admin created with username '{admin.username}'")
        return admin

    def like_post(self, post_id: int, username: str):
        """Like a post"""
        for post in self.posts:
            for like in self.likes:
                if like[0] == post_id and like[1] == username:
                    print("You have already liked this post")
                    return
            if post.author == username:
                print("You can't like your own post")
                return
            if post.id == post_id:
                for user in self.users:
                    if user.username == username:
                        post.likes += 1
                        print(f"Post '{post.title}' liked")
                        self.likes.append([post_id, username])
                        return