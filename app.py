from flask import Flask
from flask import render_template, request, flash
from dotenv import load_dotenv
from db.database import db
import os
from datetime import datetime
from sqlalchemy.exc import IntegrityError, OperationalError

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
       date_f = datetime.strptime(date,'%Y-%m-%d')
       occupation = request.form['occupation']

       form = Form(first_name=first_name,
                   last_name=last_name,
                   email=email,
                   date=date_f,
                   occupation=occupation)
       
       db.session.add(form)
       print(email, first_name)
       try:  
           db.session.commit()
           
           flash('Your Form has been submitted', 'success')
       except IntegrityError as e:
            db.session.rollback()
            flash(f'{email} is already registered','error')
            print(e)

       except OperationalError as e :
           print(e)
            
            
        

    return render_template("index.html",)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)
    