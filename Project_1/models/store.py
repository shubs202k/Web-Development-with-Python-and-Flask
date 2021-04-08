from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    # define the columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))

    # join expression of stores table with items table
    items = db.relationship('ItemModel', lazy = 'dynamic')

    def __init__(self, name):
        self.name = name

    # return store json object
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    # get store by its name
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()

    # save a store to the stores table
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # delete a store from the stores table
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
