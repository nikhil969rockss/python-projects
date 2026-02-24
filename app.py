from flask import Flask
from flask import render_template, request
from dotenv import load_dotenv
from db.database import db
import os

from models.form import Form

load_dotenv()

if not os.path.exists('.env') :
    print(".env file doesn't exit ")
    exit()
    
# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USE_SSL"] = True
# app.config["MAIL_USERNAME"] = "app8flask@gmail.com"
# app.config["MAIL_PASSWORD"] = "------YOUR EMAIL PASSWORD GOES HERE----"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY') # to secure from hijacking session, cookies
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)
    return app

app = create_app()
    
@app.route("/",methods=['GET', 'POST'])
def home_page():
    if request.method =='POST':
       first_name = request.form['first_name']
       last_name = request.form['last_name']
       email = request.form['email']
       date = request.form['date']
       occupation = request.form['occupation']

    return render_template("index.html")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)
    