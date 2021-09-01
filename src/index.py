from src.controllers.MainController import main_controller
from src.controllers.BookController import book_controller
from src.controllers.AuthorController import author_controller
from src.controllers.ReviewController import review_controller
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