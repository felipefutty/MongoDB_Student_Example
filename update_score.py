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
s_id = int(input('student id: '))

# Raad scores
s_exam = float(input('new exam score:'))
s_homework = float(input('new homework score:'))
s_quiz = float(input('new quiz score:'))

query = { "_id": s_id }

new_scores = { "scores": [
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

# Update student from mongodb
try:
    student = grades.update_one(query, {'$set': new_scores})
except Exception as e:
    print("Unexpected error:", type(e), e)
    sys.exit(0)

print("Student has been updated!")
