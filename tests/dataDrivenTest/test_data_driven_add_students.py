import os
import requests
import json
from tests.dataDrivenTest import Library

current_directory = os.getcwd()
root_folder_name = os.path.basename(current_directory)
parent_directory = current_directory.rstrip(root_folder_name)

def test_add_multiple_students():
    print(current_directory+"********************")
    API_URLS = "https://thetestingworldapi.com/api/studentsDetails"
    file = open(parent_directory + "data\studentDetailsExcel.json", 'r')
    json_request = json.loads(file.read())
    obj = Library.Common(parent_directory+"data/testData.xlsx",'Sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList  = obj.fetch_key_names()

    for i in range(1,row+1):
        updated_json_request = obj.update_request_with_data(i,json_request,keyList)
        response = requests.post(API_URLS,updated_json_request)
        print(response.status_code)
        print(response.json())
        print(parent_directory)



