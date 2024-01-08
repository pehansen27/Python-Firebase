# Peyton Hansen
# DSCI 551 Fall 2023
# HW1: Teach Course
# Firebase URL: https://peyton-hansen-hw1-default-rtdb.firebaseio.com/


import requests
import json
import sys


def validity(instructorID, numberInput, semesterInput):
    firebase = 'https://peyton-hansen-hw1-default-rtdb.firebaseio.com/'

    # check that arguments exist in firebase
    instructorValid = requests.get(firebase + 'instructor.json').json()
    numberValid = requests.get(firebase + 'course.json').json()
    semesterValid = requests.get(firebase + 'course/' + numberInput + '.json').json()

    # valid student
    if instructorValid != None:
        key1 = instructorID in instructorValid.keys()
    else:
        key1 = False

    # valid course
    if numberValid != None:
        key2 = numberInput in numberValid.keys()
    else:
        key2 = False

    # valid semester
    if semesterValid != None:
        key3 = semesterInput in semesterValid.keys()
    else:
        key3 = False

    # return boolean
    return key1, key2, key3


def teach_course(instructorID, numberInput, semesterInput):

    if validity(instructorID, numberInput, semesterInput) == (True, True, True):
        teaches = 'teaches'

        #insturctor attribute
        firebase = 'https://peyton-hansen-hw1-default-rtdb.firebaseio.com/instructor/'

        #find specific insturctor
        newUrl = f'{firebase}/{instructorID}/{teaches}'

        #add course number
        data = json.dumps(numberInput)

        #patch in the data
        response = requests.patch(newUrl + '.json', data=data)
        #print(response.status_code)

        # find specific course number of specific instructor
        newUrl2 = f'{firebase}/{instructorID}/{teaches}/{numberInput}.json'

        #patch in semester input
        values = {semesterInput: 'semester'}
        response2 = requests.patch(newUrl2, json=values)


    else:
        print('Please enter valid argument. Either the instructor, course number or semester do not exist.')
        print(validity(instructorID, numberInput, semesterInput))


if __name__ == '__main__':
    # arguments
    arguments = sys.argv
    instructorID = arguments[1].lower()
    numberInput = arguments[2].lower()
    semesterInput = arguments[3].lower()

    # call function
    teach_course(instructorID, numberInput, semesterInput)