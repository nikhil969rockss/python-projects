from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def home_page():
    if request.method =='POST':
       first_name = request.form['first_name']
       last_name = request.form['last_name']
       email = request.form['email']
       date = request.form['date']
       occupation = request.form['occupation']

       print(occupation, first_name)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)