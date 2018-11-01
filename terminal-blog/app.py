# from models.post import Post
# from models.blog import Blog
from database import Database
from menu import Menu

Database.initialize()

menu = Menu()

menu.run_menu()