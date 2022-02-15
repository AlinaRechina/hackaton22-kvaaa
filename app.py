from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/movie-by-preferences')
def similarity():
    return render_template('Movie by preferences.html')


@app.route('/more')
def more():
    return render_template('More.html')


if __name__ == '__main__':
    app.run()
