from flask import Flask

app=Flask(__name__)

DB="bookss_db"
app.secret_key="Secret Key"