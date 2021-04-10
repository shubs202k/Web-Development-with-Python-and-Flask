from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store_id."
                        )
    @jwt_required()
    def get(self, name):

        # check if item exists in the items table and return it
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {'message' : 'Item not found'}, 404

    def post(self,name):

        # check if the item already exists
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        # get the json payload info about price and store_id
        data = Item.parser.parse_args()

        # create an item object
        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save_to_db() # insert created item to items database
        except:
            return {"message": "An error occurred inserting the item."}, 500

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted'}
        return {'message': 'Item not found'}, 404

    def put(self,name):
        # get the json payload info about price and store_id
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price'] # update if item exits
        else:
            item = ItemModel(name, data['price'], data['store_id']) # create item

        # save updated/newly created item to the table
        item.save_to_db()

        return item.json()


class ItemList(Resource):

    # get all items from the items table
    def get(self):
        return {'items' : [item.json() for item in self.items.all()]}
