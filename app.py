from flask import Flask, render_template, request, flash, redirect, url_for
from routes.post import post_pages
from sqlmodel import SQLModel, create_engine
from models.post import Post


      
app = Flask(__name__, static_folder='static')
app.engine = create_engine("sqlite:///database.db") 
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


        

@app.before_request
def create_db():
    SQLModel.metadata.create_all(app.engine)


app.register_blueprint(post_pages)

if __name__ == '__main__':
    app.run(debug=True)