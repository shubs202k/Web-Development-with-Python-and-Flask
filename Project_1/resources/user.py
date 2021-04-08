from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    # parser to parse username and password from json payload
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self, name):

        # get username and password from json payload
        data = UserRegister.parser.parse_args()

        # check if user already exists
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        # if user does not exist, create a new user and save to users table in database
        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201
