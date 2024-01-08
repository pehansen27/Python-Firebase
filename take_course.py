# Peyton Hansen
# DSCI 551 Fall 2023
# HW1: Take Course
# Firebase URL: https://peyton-hansen-hw1-default-rtdb.firebaseio.com/


import requests
import json
import sys


def validity(studentID, numberInput, semesterInput):
    firebase = 'https://peyton-hansen-hw1-default-rtdb.firebaseio.com/'

    #check that arguments exist in firebase
    studentValid = requests.get(firebase + 'student.json').json()
    numberValid = requests.get(firebase + 'course.json').json()
    semesterValid = requests.get(firebase + 'course/' + numberInput + '.json').json()

    #valid student
    if studentValid != None:
        key1 = studentID in studentValid.keys()
    else:
        key1 = False

    #valid course
    if numberValid != None:
        key2 = numberInput in numberValid.keys()
    else:
        key2 = False

    #valid semester
    if semesterValid != None:
        key3 = semesterInput in semesterValid.keys()
    else:
        key3 = False

    #return boolean
    return key1, key2, key3

def take_course(studentID, numberInput, semesterInput):

    if validity(studentID,numberInput,semesterInput) == (True, True, True):
        takes = 'takes'
        student = 'student'

        # student attribute
        firebase = 'https://peyton-hansen-hw1-default-rtdb.firebaseio.com/'

        # find specific student
        newUrl = f'{firebase}/{student}/{studentID}/{takes}'

        # patch in number of class specific student takes
        data = json.dumps(numberInput)
        response = requests.patch(newUrl + '.json', data=data)
        #print(response.status_code)

        # find specific course number of specific student
        newUrl2 = f'{firebase}/{student}/{studentID}/{takes}/{numberInput}.json'

        # patch in semester
        values = {semesterInput: 'semester'}
        response2 = requests.patch(newUrl2, json=values)
        #print(response2.status_code)


    else:
        print('Please enter valid argument. Either the student, course number or semester do not exist.')
        print(validity(studentID,numberInput,semesterInput))


if __name__ == '__main__':
    # arguments
    arguments = sys.argv
    studentID = arguments[1].lower()
    numberInput = arguments[2].lower()
    semesterInput = arguments[3].lower()

    # call function
    take_course(studentID, numberInput, semesterInput)

