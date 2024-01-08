# Peyton Hansen
# DSCI 551 Fall 2023
# HW1: Find Student Courses
# Firebase URL: https://peyton-hansen-hw1-default-rtdb.firebaseio.com/


import requests
import json
import sys

def find_student_courses(studentID):
    # firebase
    firebase = 'https://peyton-hansen-hw1-default-rtdb.firebaseio.com/student/'

    # find student
    newUrl = f'{firebase}/{studentID}.json'
    find = requests.get(newUrl)

    # create output
    if find.status_code == 200:
        data = find.json()
        if data:
            name = data.get('name','')
            takes = data.get('takes', {})
            courses = []
            for course, semester in takes.items():
                for sem in semester:
                    courseData = {'course': course, 'semester': sem}
                    courses.append(courseData)
            info = {'name': name, 'courses': courses}
            print(json.dumps(info))
        else:
            print('Student information missing.')
    else:
        print('Student information missing.')


if __name__ == '__main__':
    # arguments
    arguments = sys.argv
    studentID = arguments[1].lower()

    # call function
    find_student_courses(studentID)
