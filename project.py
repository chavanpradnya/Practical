from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://hr:hr@127.0.0.1:1521/xe'
db = SQLAlchemy(app)


class Student(db.Model):
    stuid = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    marks = db.Column(db.Integer(), unique=False, nullable=False)


@app.route("/stuinfo", methods=['GET', 'POST'])
def stuInfo():
    if request.method =='POST':
        'add entry to DB'
        stuid = request.form.get('stuid')
        name = request.form.get('name')
        marks = request.form.get('marks')

        entry = Student(stuid=stuid, name=name, marks=marks)
        db.create_all()
        db.session.add(entry)
        db.session.commit()

    return render_template('stuinfo.html')


if __name__ == "__main__":
    app.run(debug=True)
