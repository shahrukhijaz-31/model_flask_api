from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()


@app.route('/')
def show_all():
    data = User.query.all()
    return render_template('show_all.html', Users=data)

@app.route('/add_user')
def add_user():
    return render_template("insert.html")


@app.route('/insert', methods=['POST'])
def insert():
    name = request.form['name']
    email = request.form['email']
    new_user = User(username=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('show_all'))


@app.route('/delete/<id>', methods=['GET'])
def delete(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('show_all'))


@app.route('/edit/<id>', methods=['GET'])
def edit(id):
    user = User.query.filter_by(id=id).first()
    return render_template("edit.html", user=user)

@app.route('/update', methods=['POST'])
def update():
    name = request.form['name']
    email = request.form['email']
    return "hello"

if __name__ == '__main__':
    app.run()
