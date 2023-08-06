from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identify
from resources.user import UserRegister
from resources.item import Item,ItemLsit
from resources.stores import StoreList, Store



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'psajsndks'
api = Api(app)
jwt = JWT(app,authenticate,identify) 
api.add_resource(Store,'/store/<string:name>')     
api.add_resource(ItemLsit,'/items')    
api.add_resource(Item,'/item/<string:name>')
api.add_resource(UserRegister,'/register')
api.add_resource(StoreList,'/stores') 

@app.before_request
def create_tables():
    
    db.create_all()

if __name__ == '__main__':
    from db import db
    db.init_app(app) 
    app.run(port=5000,debug=True)
    db.create_all()
    
