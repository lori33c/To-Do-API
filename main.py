from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Create a connection to the MongoDB database
client = MongoClient('mongodb://localhost:27017')
db = client['todolistdb']
task = db['tasks'] #this is our task collection inside the db

# Clear the existing tasks in the collection
task.delete_many({})

my_task = {
    "name" : 'wash cat',
    "description" : 'put soap on cat and hose down',
    "rank" : 1
}

inserted_task = db.tasks.insert_one(my_task)


@app.get("/")
def root():
    return {"message" : "Hello, world!"}