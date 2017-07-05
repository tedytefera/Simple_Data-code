from flask import Flask
from flask import render_template, request, redirect, url_for
from nn import*

app = Flask(__name__)

@app.before_request
def before_request():
    initialize_db()

@app.teardown_request
def teardown_request(exception):
    db.close()

@app.route('/')
def Myweb():
    return render_template('home.html', teddy=Call.select().order_by(Call.date.desc()))

@app.route('/index/')
def index():
    return render_template('mm.html')

@app.route('/create/', methods=["POST"])
def create_post():
    Call.create(
       title=request.form['title'],
       text=request.form['text']
    )
    return redirect(url_for('Myweb'))
       


if __name__ =='__main__':
   app.run(debug=True)


