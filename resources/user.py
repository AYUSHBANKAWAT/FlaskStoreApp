import sqlite3
from flask_restful import Resource,reqparse
from models.users import UserModel

      
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        help="This field cannot be blank"   
    )
    parser.add_argument(
        'password',
        type=str,
        help="This field cannot be blank"
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"message":"A User with that name already exist."}
        user  = UserModel(**data)
        user.save_to_db()
        return {"message":"User created Succesfully"}
    
    