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
s_name = input('student name:')
s_id = int(input('student id: '))
s_exam = float(input('student exam score:'))
s_homework = float(input('student homework score:'))
s_quiz = float(input('student quiz score:'))

# Define student
new_student = {
    "_id": s_id, 
    "name": s_name, 
    "scores": [
        {
            "type": "exam",
            "score": s_exam
        },
        {
            "type": "homework",
            "score": s_homework
        },
        {
            "type": "quiz",
            "score": s_quiz
        }
     ]
}

# Retrieve student from mongodb
try:
    student = grades.insert_one(new_student)
except Exception as e:
    print("Unexpected error:", type(e), e)
    sys.exit(0)

print("Student has been inserted!")
