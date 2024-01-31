from flask import Flask, render_template, request
from .models.database import init_db, db
from .models.post import Post

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}'.format(**{
    'user':'gawa',
    'password':'root',
    'host':'localhost',
    'db_name':'mysql_database'
})

@app.route("/")
def index():
    return render_template('main.html')

@app.route("/sub")
def sub():
    return render_template('sub.html')



if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')


# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)



# class User(db.Model):
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)

# class Post(db.Model):
#     __tablename__ = "post"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(30), nullable=False)
#     body = db.Column(db.String(500), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     user = db.relationship("User", backref="posts", lazy="True")

