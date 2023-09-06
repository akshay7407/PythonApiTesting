import os

import requests
import json
import jsonpath

current_directory = os.getcwd()
root_folder_name = os.path.basename(current_directory)
parent_directory = current_directory.rstrip(root_folder_name)

def test_add_student_details():
    global id
    API_URLS = "https://thetestingworldapi.com/api/studentsDetails"
    file = open(parent_directory + "data/studentDetails.json", 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URLS, json_request)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

def test_update_student_data():
    API_URLS = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    file = open(parent_directory + "data/studentDetails.json", 'r')
    json_request = json.loads(file.read())
    response = requests.put(API_URLS,json_request)
    print(response.text)

def test_get_student_data():
    API_URLS = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(API_URLS)
    json_response = json.loads(response.text)
    print(json_response)
    lastName= jsonpath.jsonpath(json_response, 'data.last_name')
    assert lastName[0] == "Gaikwad"

def test_delete_data():
    API_URLS = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.delete(API_URLS)
    print(response.text)



