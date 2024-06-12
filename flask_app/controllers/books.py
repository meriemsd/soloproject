from flask_app import app
from flask import render_template , request , redirect, session

from flask_app.models.book import Book
from flask_app.models.user import User

@app.route("/")
def index():
    return redirect('/books')



@app.route('/books')
def books():

    books=Book.get_all()

    return render_template("newbook.html" , books = books)



@app.route("/books/create" , methods=['POST'])
def create_book():
    Book.create(request.form)
    return redirect('/book')


@app.route("/books/update" , methods=['POST'])
def update_book():
    Book.update(request.form)
    return redirect('/books')



@app.route("/books/delete" , methods=['POST'])
def delete_book():
    data={'id' : id}
    book = Book.get_by_id(data)
    if book.user.id == session['user_id']:
        Book.delete(data)
    return redirect('/book')



@app.route("/books/<int:id>")
def bookname():
    return render_template("creator.html")