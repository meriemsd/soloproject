from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask_app.models.user import User
from flask import flash



class Book:
    def __init__(self , data):
        self.id= data["id"]
        self.reader = data["reader"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at=data["updated_at"]
        self.user = None

    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM books JOIN users ON books.user_id = users.id WHERE books.id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)

        book = None
        if result:
            book = cls(result[0])
            user_data ={

                    'id': result[0]['users.id'],
                    'first_name': result[0]['first_name'],
                    'last_name': result[0]['last_name'],
                    'email': result[0]['email'],
                    'password': result[0]['password'],
                    'updated_at': result[0]['users.updated_at'],
                    'created_at': result[0]['users.created_at']
                    
            }
            book.user = User(user_data)
        return book

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books JOIN users ON books.user_id = users.id"
        results = connectToMySQL(DB).query_db(query)

        books = []
        if results:
            for row in results:
                book = cls(row)
                user_data={
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['users.created_at'],


                }
                book.user = User(user_data)
                books.append(book)
        return books
    

    @classmethod
    def create(cls , data):
        query = "INSERT INTO books (name , reader , description , user_id) VALUES (%(name)s , %(reader)s , %(description)s , %(user_id)s);" 
        result = connectToMySQL(DB).query_db(query , data)
        return result



    @classmethod
    def update(cls, data):
        query= "UPDATE books SET name= %(name)s, reader= %(reader)s, description=%(description)s, user_id=%(user_id)s WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    


    @classmethod
    def delete(cls , data):
        query = "DELETE FROM books WHERE id = %(id)s;" 
        result = connectToMySQL(DB).query_db(query , data)
        return result
    
