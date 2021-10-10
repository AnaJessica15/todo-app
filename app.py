from flask import Flask,render_template, jsonify,redirect, request, url_for
from dotenv import load_dotenv
import json
import pymongo
from pymongo import MongoClient
import os

load_dotenv()
MONGO_URI    = os.environ.get("MONGO_URI") 

# MONGO_URI   = os.getenv("MONGO_URI")
# MONGO_URI="mongodb+srv://admin-Ishita:ishita@cluster0.266b1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster  = MongoClient(MONGO_URI)

db = cluster["productivity-app"]
col = db["todo"]
app  = Flask(__name__)

# def get_week_num(date):
#     year,week_num,day_of_week = date.isocalendar()
#     # print(week_num)
#     return week_num

@app.route("/", methods=["GET","POST"])
def startpy():
    
    content=request.form.get("todo-input")

    todo = {
        "todo"   : content
        
    }

    x = col.insert_one(todo)
    print(x)

    # for x in col.find():
    #     col.delete_one(x)
    #     print(x)

    data =[]
    x =col.find({})
    for y in x:
        data.append(y)
    # print(data)

    # result = col.find_one()
    # for x in col.find({}):
    #     print(x)
    return render_template('index.html', result = data, delete = x)

if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0")
