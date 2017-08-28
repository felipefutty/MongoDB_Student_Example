#!/usr/bin/env python
import json
import pymongo
import sys

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit database
db = connection.student
grades = db.grades

# Read student id
s = input('student id: ')

# Define delete query
query = {"_id" : int(s)}

# Delete student from mongodb
try:
    result = grades.delete_one(query)
except Exception as e:
    print("Unexpected error:", type(e), e)
    sys.exit(0)

# Print output
print("Student has been deleted!")
