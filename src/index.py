from src.persistence.models.Author import Author, AuthorSchema
from src.persistence.models.Review import Review, ReviewSchema
from flask.json import jsonify
from app import create_app
from src.persistence.models.Book import Book, BookSchema
from flask import request
import os

settings_module = os.getenv('APP_SETTIGNS_MODULE')
app = create_app(settings_module)

book_schema = BookSchema()
review_schema = ReviewSchema()
author_schema = AuthorSchema()

@app.route('/')
def main():
  return "<h1>Hello. Welcome to ReBooks 😊.</h1>", 200

@app.route('/books', methods=['GET'])
def get_books():
  books = Book.get_all()
  result = book_schema.dump(books, many=True)
  return jsonify(result), 200

@app.route('/books', methods=['POST'])
def add_book():
  data = request.get_json()
  new_book:Book = book_schema.load(data)
  book = Book(name=new_book.name,
              cover=new_book.cover,
              abstract=new_book.abstract,
              publication_date=new_book.publication_date,
              reviews=new_book.reviews
              )
  book.save()
  response = book_schema.dump(book)
  return jsonify(response), 201

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id:int):
  book = Book.get_by_id(id)
  book.delete()
  return 'Book deleted', 200

@app.route('/reviews', methods=['GET'])
def get_reviews():
  reviews = Review.get_all()
  result = review_schema.dump(reviews, many=True)
  return jsonify(result), 200

@app.route('/reviews', methods=['POST'])
def add_review():
  data = request.get_json()
  print(data)
  new_review:Review = review_schema.load(data)
  review = Review(content=new_review.content, publication_date=new_review.publication_date, book_id=new_review.book_id)
  review.save()
  response = review_schema.dump(review)
  return jsonify(response), 201

@app.route('/reviews/<id>', methods=['DELETE'])
def delete_review(id:int):
  review = Review.get_by_id(id)
  review.delete()
  return 'Review deleted', 200

@app.route('/authors', methods=['GET'])
def get_authors():
  authors = Author.get_all()
  result = author_schema.dump(authors, many=True)
  return jsonify(result), 200

@app.route('/authors', methods=['POST'])
def add_author():
  data = request.get_json()
  new_author:Author = author_schema.load(data)
  author = Author(name=new_author.name)
  author.save()
  response = author_schema.dump(author)
  return jsonify(response), 201

@app.route('/authors/<id>', methods=['DELETE'])
def delete_authors(id:int):
  author = Author.get_by_id(id)
  author.delete()
  return 'Author deleted', 200