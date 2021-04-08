from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    # define the columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))

    # join with stores table using id
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.store_id = store_id

    # return the item object in json
    def json(self):
        return {'name': self.name, 'price': self.price}

    # find item by its name from items table
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name = name).first()

    # save an item to the items table
    def save_to_db(self):
        self.session.add(self)
        self.session.commit()

    # delete an item from items table
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
