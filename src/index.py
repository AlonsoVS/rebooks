from src.persistence.models.Author import Author, AuthorSchema
from src.persistence.models.Review import Review, ReviewSchema
from flask.json import jsonify
from app import create_app, db
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

@app.route('/books/<id>', methods=['GET'])
def get_book(id:int):
  book = Book.get_by_id(id)
  if book is not None:
    result = book_schema.dump(book)
    return jsonify(result), 200
  return 'Book not found', 404

@app.route('/books', methods=['POST'])
def add_book():
  data = request.get_json()
  new_book:Book = book_schema.load(data)
  book = Book(name=new_book.name,
              cover=new_book.cover,
              abstract=new_book.abstract,
              publication_date=new_book.publication_date,
              reviews=new_book.reviews)

  for author in new_book.authors:
    if author.id is None:
      book.authors.append(Author(author.name))
    else:
      author_found = author.get_by_id(author.id)
      if (author_found is not None):
        book.authors.append(author_found)
      else:
        return f'The author with id: {author.id} doesn´t exists', 409
  
  for review in new_book.reviews:
    book.reviews.append(Review(content=review.content, 
                              publication_date=review.publication_date))
  book.save()
  db.session.commit()
  response = book_schema.dump(book)
  return jsonify(response), 201

@app.route('/books/<id>', methods=['PUT'])
def edit_book(id:int):
  updated_book = request.get_json()
  if id is not None:
    book_found:Book = db.session.query(Book).get(id)
    if book_found is not None:
      for key in updated_book.keys():
        try:
          setattr(book_found, key, updated_book[key])
        except:
          return f'The {key} property cannot be modified', 400
    else:
      return 'Book not found', 404
    db.session.commit()
    response = book_schema.dump(book_found)
  return jsonify(response), 200

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

@app.route('/reviews/<id>', methods=['GET'])
def get_review(id):
  review = Review.get_by_id(id)
  if review is not None:
    result = review_schema.dump(review)
    return jsonify(result), 200
  return 'Review not found', 404

@app.route('/reviews', methods=['POST'])
def add_review():
  data = request.get_json()
  new_review:Review = review_schema.load(data)
  review = Review(content=new_review.content,
                  publication_date=new_review.publication_date,
                  book_id=new_review.book_id)
  review.save()
  response = review_schema.dump(review)
  return jsonify(response), 201

@app.route('/reviews/<id>', methods=['PUT'])
def edit_review(id:int):
  updated_review = request.get_json()
  if id is not None:
    review_found:Review = db.session.query(Review).get(id)
    if review_found is not None:
      for key in updated_review.keys():
        try:
          setattr(review_found, key, updated_review[key])
        except:
          return f'The {key} property cannot be modified'
    else:
      return 'Review not found', 404
    db.session.commit()
    response = review_schema.dump(review_found)
  return jsonify(response), 200

@app.route('/reviews/<id>', methods=['DELETE'])
def delete_review(id:int):
  review = Review.get_by_id(id)
  if review is not None:
    review.delete()
    return 'Review deleted', 200
  return 'Review not found', 404

@app.route('/authors', methods=['GET'])
def get_authors():
  authors = Author.get_all()
  result = author_schema.dump(authors, many=True)
  return jsonify(result), 200

@app.route('/authors/<id>', methods=['GET'])
def get_author(id):
  author = Author.get_by_id(id)
  if author is not None:
    result = author_schema.dump(author)
    return jsonify(result), 200
  return 'Author not found', 404

@app.route('/authors', methods=['POST'])
def add_author():
  data = request.get_json()
  new_author:Author = author_schema.load(data)
  author = Author(name=new_author.name)
  author.save()
  response = author_schema.dump(author)
  return jsonify(response), 201

@app.route('/authors/<id>', methods=['PUT'])
def edit_author(id:int):
  updated_author = request.get_json()
  if id is not None:
    author_found:Author = db.session.query(Author).get(id)
    if author_found is not None:
      for key in updated_author.keys():
        try:
          setattr(author_found, key, updated_author[key])
        except:
          return f'The {key} property cannot be modified'
    else:
      return 'Author not found', 404
    db.session.commit()
    response = author_schema.dump(author_found)
  return jsonify(response), 200

@app.route('/authors/<id>', methods=['DELETE'])
def delete_authors(id:int):
  author = Author.get_by_id(id)
  if author is not None:
    author.delete()
    return 'Author deleted', 200
  return 'Author not found', 404