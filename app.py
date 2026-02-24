from flask import Flask
from flask import render_template, request, flash,redirect,url_for
from dotenv import load_dotenv
from db.database import db
import os
from datetime import datetime
from sqlalchemy.exc import IntegrityError, OperationalError
from flask_mail import Mail, Message

from models.form import Form

load_dotenv()

if not os.path.exists('.env') :
    print(".env file doesn't exit ")
    exit()
    
mail= Mail()
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY') # to secure from hijacking session, cookies
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = os.getenv('SENDER_EMAIL')
    app.config["MAIL_PASSWORD"] = os.getenv('APP_PASSWORD')
    db.init_app(app)
    mail.init_app(app)
    
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

       form = Form(first_name=first_name, # type: ignore
                   last_name=last_name,   # type: ignore
                   email=email,           # type: ignore
                   date=date_f,           # type: ignore
                   occupation=occupation) # type: ignore
       
       db.session.add(form)
       
       try:
            db.session.commit()
            
            message_body = f"""Thank You For Registring Our Job Portal {first_name}\n
            Your details are as follows:\n {first_name} {last_name}\n{email}\n{date}\n{occupation},
            we will keep you updated about the job openings"""
           
            message = Message(subject="Job Portal Registeration", 
                             sender=app.config['MAIL_USERNAME'],
                             recipients=[email,],
                             body=message_body)
            mail.send(message=message)
           
           
            flash('Your Form has been submitted', 'success')
            
            return redirect(url_for('home_page'))

       except IntegrityError as e:
           db.session.rollback()
           print(e)
           flash('This email is already registered','error')
           
       except OperationalError as e :
           print(e)

    
    return render_template('index.html')
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)
    