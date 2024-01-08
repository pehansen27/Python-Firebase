# Peyton Hansen
# DSCI 551 Fall 2023
# HW1: Find Instructor Courses
# Firebase URL: https://peyton-hansen-hw1-default-rtdb.firebaseio.com/


import requests
import json
import sys


def find_instructor_courses(instructorID):
    # firebase
    firebase = 'https://peyton-hansen-hw1-default-rtdb.firebaseio.com/instructor/'

    # find instructor
    newUrl = f'{firebase}/{instructorID}.json'
    find = requests.get(newUrl)

    # create output
    if find.status_code == 200:
        data = find.json()
        if data:
            name = data.get('name','')
            teaches = data.get('teaches', {})
            courses = []
            for course, semester in teaches.items():
                for sem in semester:
                    courseData = {'course': course, 'semester': sem}
                    courses.append(courseData)
            info = {'name': name, 'courses': courses}
            print(json.dumps(info))
        else:
            print('Instructor information missing.')
    else:
        print('Instructor information missing.')

if __name__ == '__main__':
    # arguments
    arguments = sys.argv
    instructorID = arguments[1].lower()

    # call function
    find_instructor_courses(instructorID)