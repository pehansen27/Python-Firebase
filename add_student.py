# Peyton Hansen
# DSCI 551 Fall 2023
# HW1: Add Student
# Firebase URL: https://peyton-hansen-hw1-default-rtdb.firebaseio.com/


import requests
import json
import sys

def add_student(idInput, nameInput, programInput):

	#url
	firebase = 'https://peyton-hansen-hw1-default-rtdb.firebaseio.com/student'

	#added input
	values = {idInput:{'name': nameInput, 'program': programInput}}
	data = json.dumps(values)

	#patch in input
	req = requests.patch(firebase + '.json', data = data)
	# print(res.content)


if __name__ == '__main__':
	# arguments
	arguments = sys.argv
	idInput = arguments[1].lower()
	nameInput = arguments[2].lower()
	programInput = arguments[3].lower()

	# call function
	add_student(idInput, nameInput, programInput)



