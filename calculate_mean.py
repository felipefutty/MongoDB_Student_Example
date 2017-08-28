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

# Define query
query = {"_id" : int(s)}

# Retrieve student from mongodb
try:
    student = grades.find_one(query)
except Exception as e:
    print("Unexpected error:", type(e), e)
    sys.exit(0)

if student == None:
   print("Student has not been found!")
   sys.exit(0)

# Caculate the mean
mean = 0.0
error = False
for item in student['scores']:
    weight = 0.0
    if item['type'] == "homework":
        weight = 2.0
    elif item['type'] == "exam":
        weight = 3.0
    elif item['type'] == "quiz":
        weight = 1.0
    else:
        print("Type score error:", item['type'])
        error = True
        break

    if isinstance(item['score'], float): 
        mean = mean + (weight * item['score'])
    else:
        print("Not recognized score:", item['score'])
        error = True
        break

# Print output
print("### %s ###" % student['name'])
if error:
    print("Could not stimate the student mean:", student)
else:
    mean = mean / 6.0
    print("Student mean:", mean)
