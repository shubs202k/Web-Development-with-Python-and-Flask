from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # search for a user with username in the users table
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    # add user to the users table
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # search for a user with id in the users table
    @classmethod
    def find_By_id(cls, _id):
        return cls.query.filter_by(id = _id).first()
