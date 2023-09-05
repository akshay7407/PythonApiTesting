import  json

import jsonpath
import requests
import os

current_directory = os.getcwd()
root_folder_name = os.path.basename(current_directory)
parent_directory = current_directory.rstrip(root_folder_name)

def test_end_to_end_flow():
    API_URLS = "https://thetestingworldapi.com/api/studentsDetails"
    file = open(parent_directory + "data/studentDetails.json", 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URLS, json_request)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])
    print(response.text)

    TECHSKILL_URL ="https://thetestingworldapi.com/api/technicalskills"
    file = open(parent_directory + "data/technical.json", 'r')
    json_request = json.loads(file.read())
    json_request['id'] = id[0]
    json_request['st_id'] = id[0]
    response = requests.post(TECHSKILL_URL, json_request)
    print(response.text)

    ADDRESS_URL = "https://thetestingworldapi.com/api/addresses"
    file = open(parent_directory + "data/address.json", 'r')
    json_request = json.loads(file.read())
    json_request['stId'] = id[0]
    response = requests.post(ADDRESS_URL, json_request)
    print(response.text)

    FINAL_DETAILS_URL = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])+""
    response = requests.get(FINAL_DETAILS_URL)
    print(response.text)

