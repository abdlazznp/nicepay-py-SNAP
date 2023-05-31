# class TestingSNAP :
#     def __init__(self):
#         self.xTimestamp = None
#         self.xClientKey = None
#         self.xSignature = None

import requests
import json 

class TESTINGAPI :
    def get_data(self,api):
        response = request.get(f"{api}")
        if response.status_code == 200:
            print("successfully fetched the data")
            self.formatted_print(response.json())
        else :
            print(f"Response Code : {response.status_code}")
    
    def get_user_data(self, api, parameters):
        response = requests.get(f"{api}", params=parameters)
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self, api):
        # self.get_data(api)

        parameters = {
            "username": "kedark"
        }
        self.get_user_data(api, parameters)

if __name__ == "__main__":
    api_call = TESTINGAPI("https://dev.nicepay.co.id/nicepay/direct/v2/registration")