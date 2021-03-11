from flask import Flask, render_template,request
from get_em import NameGetter
app = Flask(__name__)
s = NameGetter()
@app.route('/',methods = ['GET','POST'])
def send():
    if request.method == 'POST':
        age = request.form['age']
        return render_template('blimp.html',age=s.getmatch(age))
    return render_template('index.html')

if __name__ == '__main__':
    app.run()