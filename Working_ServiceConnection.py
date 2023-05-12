import os
import numpy as np
import requests
import json
import base64

def ServiceConnection(Organization, Project, Personal_Access_Token):
    authorization = base64.b64encode(Personal_Access_Token.encode()).decode()
    headers_ServiceConnection = {
        "Content-Type": "application/json",
        "Authorization": "Basic" + authorization
    }
    url_connectionapi = f"https://dev.azure.com/{Organization}/_apis/serviceendpoint/endpoints?api-version=7.0"

    payload_connectionapi = {
        "data": {},
        "name": "SonarQube",
        "type": "SonarQube",
        "url": "http://43.205.124.128:9000/",
        "authorization": {
            "parameters": {
                "password": "null",
                "username": "myusername",
            },
            "scheme": "UsernamePassword",
        },
        "isShared": False,
        "isReady": True,
        "serviceEndpointProjectReferences": [
            {
                "projectReference": {
                    "id": "",
                    "name": "DevOps_Tech"
                },
                "name": "sonar_cloud"
            }
        ]
    }
    
    existing_connections = requests.get(url_connectionapi, headers=headers_ServiceConnection).json()
    
    # for connection in existing_connections.get('value', []):
    #     if connection.get('name') == 'SonarQube':
    #         payload_connectionapi['id'] = connection.get('id')
    #         payload_connectionapi['revision'] = connection.get('revision')
    #         payload_connectionapi['serviceEndpointProjectReferences'][0]['projectReference']['id'] = connection.get('serviceEndpointProjectReferences')[0].get('projectReference').get('id')
    #         break

    # if not payload_connectionapi['serviceEndpointProjectReferences'][0]['projectReference']['id']:
    #     projects_url = f"https://dev.azure.com/{Organization}/_apis/projects?api-version=6.0"
    #     projects_response = requests.get(projects_url, headers=headers_ServiceConnection)
    #     projects = projects_response.json()['value']
    #     for project in projects:
    #         if project['name'] == Project:
    #             payload_connectionapi['serviceEndpointProjectReferences'][0]['projectReference']['id'] = project['id']
    #             break          

    json_str = json.dumps(payload_connectionapi)
    responce = requests.post(url_connectionapi, headers=headers_ServiceConnection, data=json_str)
    responce.text
    print("Service connection created successfully")
    
def main():
    Organization = "CloudaeonMVP"
    Project = "DevOps_Tech"
    Personal_Access_Token = ":lreolztykrl34d4mocvltbtmj7rptx7xcii7lwyftahbdomfdbwq"
    ServiceConnection(Organization, Project, Personal_Access_Token)


if __name__ == "__main__":
    main()
