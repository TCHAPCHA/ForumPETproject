import forum

my_forum = forum.Forum("GitHub")
my_forum.create_user("CrazyJohn125", "johny125@gmail.com")
admin = my_forum.create_admin("TCHAPCHA", "tchapcha@github.com")
user = my_forum.create_user("AlexanderTupolov", "tupolovalex@github.com")
johns_post = my_forum.create_post("Hello", "Hi, how are you?", "CrazyJohn125")
tchapchas_post = my_forum.create_post("GitHub", "Hello, how can I upload my repo on GitHub?", "TCHAPCHA")
my_forum.like_post(0, "TCHAPCHA")
my_forum.like_post(0, "TCHAPCHA")
my_forum.like_post(1, "TCHAPCHA")
my_forum.like_post(1, "AlexanderTupolov")
my_forum.like_post(0, "AlexanderTupolov")

