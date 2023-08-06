import sqlite3
from flask import  request
from flask_restful import Resource,reqparse
from flask_jwt import JWT,jwt_required
from models.items import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
    'price',
     type=float,
     required=True,
     help="This field cannot be left blank"
     )
    
    parser = reqparse.RequestParser()
    parser.add_argument(
    'store_id',
     type=int,
     required=True,
     help="Every item needs a store id"
     )
    
    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        
        if item:
            return item.json()
        return {'meassage':'No such item Exist'} 
         
    def post(self,name):
        if ItemModel.find_by_name(name):
            return ({'message':"An item with this name '{}' already exist".format(name)}), 400
        requesData = Item.parser.parse_args()
        requesData = request.get_json()
        item = ItemModel(name,**requesData)
        try:
            item.save_to_db()
        except:
            return {"message":"An error occured!!"}    
        return item.json(), 201
    
    
        
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message":"Item named as '{}' is deleted".format(name)}
        return {"message":"No such user Exist"}
    
    def put(self,name):
        requestData = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item=ItemModel(name,**requestData)   
        else:
           item.price = requestData['price']
        
        item.save_to_db()
        return item .json()
            
    
class ItemLsit(Resource):
    def get(self):
        return {'items': item.json() for item in ItemModel.query.all() }