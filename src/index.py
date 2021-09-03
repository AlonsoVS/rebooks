from src.app.main.infrastructure.controller.MainController import main_controller
from src.app.book.infrastructure.controller.BookController import book_controller
from src.app.author.infrastructure.controller.AuthorController import author_controller
from src.app.review.infrastructure.controller.ReviewController import review_controller

from app import create_app
from flask_restful import Api
import os

settings_module = os.getenv('APP_SETTIGNS_MODULE')
app = create_app(settings_module)
app.register_blueprint(main_controller)
app.register_blueprint(book_controller)
app.register_blueprint(author_controller)
app.register_blueprint(review_controller)

api = Api(app)