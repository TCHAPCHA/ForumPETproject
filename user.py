import forum

class User:
    def __init__(self, username: str, email: str):
        """Initialize a new user"""
        self.username = username
        self.email = email

class Admin(User):
    def __init__(self, username: str, email: str):
        """Initialize a new admin"""
        super().__init__(username, email)
        self.is_admin = True

    def delete_account(self, username: str):
        """Delete an account"""
        for user in forum.Forum.users:
            if user.username == username:
                forum.Forum.users.remove(user)
                print(f"Account '{username}' deleted")
                return
        print("User not found")