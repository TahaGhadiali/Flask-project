from flask import Flask ,request,jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client.test

collection = db['flask-tutorial']


db = client['todo_db']
collection = db['todo_items']

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form['itemName']
    item_desc = request.form['itemDescription']
    collection.insert_one({'name': item_name, 'description': item_desc})
    return 'Item Added Successfully!'






# @app.route('/time')
# def time():
#     current_time = datetime.now().strftime('%H:%M:%S')
#     return current_time
@app.route('/submit',methods=['POST'])
def submit():
    form_data = dict(request.json)
    
    collection.insert_one(form_data)
    
    return 'Data submitted successfully!'


@app.route('/view')
def view():
    data = collection.find()
    
    data = list(data)
    
    for items in data:
        print(items)
        
        del items['_id']
        
    data = {
        'data':data
    }
    return jsonify(data)
    
if __name__ == '__main__':
     app.run(host='127.0.0.1',port=9000,debug=True)