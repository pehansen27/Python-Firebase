# Peyton Hansen
# DSCI 551 Fall 2023
# HW1: Add Course
# Firebase URL: https://peyton-hansen-hw1-default-rtdb.firebaseio.com/


import requests
import json
import sys

def add_course(courseID, titleInput, semesterInput):

    # url
    firebase = 'https://peyton-hansen-hw1-default-rtdb.firebaseio.com/course'
    url = f'{firebase}/{courseID}.json'

    # added input
    values = {'title': titleInput, semesterInput: 'semester'}

    # patch in input
    req = requests.patch(url, json=values)


if __name__ == '__main__':
    # arguments
    arguments = sys.argv
    courseID = arguments[1].lower()
    titleInput = arguments[2].lower()
    semesterInput = arguments[3].lower()

    # call function
    add_course(courseID, titleInput, semesterInput)