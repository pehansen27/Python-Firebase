# Peyton Hansen
# DSCI 551 Fall 2023
# HW1: Add Instructor
# Firebase URL: https://peyton-hansen-hw1-default-rtdb.firebaseio.com/


import requests
import json
import sys

def add_instructor(instructorID, nameInput, departmentInput):

    #url
    firebase = 'https://peyton-hansen-hw1-default-rtdb.firebaseio.com/instructor'

    #added input
    values = {instructorID: {'name': nameInput, 'department': departmentInput}}
    data = json.dumps(values)

    #patch in input
    req = requests.patch(firebase + '.json', data=data)


if __name__ == '__main__':
    # arguments
    arguments = sys.argv
    instructorID = arguments[1].lower()
    nameInput = arguments[2].lower()
    departmentInput = arguments[3].lower()

    # call function
    add_instructor(instructorID, nameInput, departmentInput)