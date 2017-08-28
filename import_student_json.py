#!/usr/bin/env python
import json
import pymongo

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit database
db = connection.student
grades = db.grades

# drop existing collection
grades.drop()

# read json
with open('student.json') as data_file:    
    parsed = json.load(data_file)

# iterate through every news item on the page
for item in parsed:
    # put it in mongo
    grades.insert_one(item)
