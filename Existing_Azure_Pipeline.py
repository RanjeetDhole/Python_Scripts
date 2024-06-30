import os
import requests
import json
import base64


def Authentication_ReCreation(Organization, Project, Repository, Yaml_File, Pipeline_Name, Personal_Access_Token):
    
    url_repoapi = f"https://dev.azure.com/{Organization}/{Project}/_apis/git/repositories/{Repository}?api-version=6.0"
    
    authorization = base64.b64encode(Personal_Access_Token.encode()).decode()
    
    payload_reloadapi = {}
    headers_repoapi = {
        'Authorization': 'Basic ' + authorization,
    }

    headers_pipelineapi = {
    'Authorization': 'Basic '+ authorization,
    'Content-Type': 'application/json'
    }    
    
    
    response_repoapi = requests.request("GET",url_repoapi,headers=headers_repoapi)
    
    url_pipelineapi = f"https://dev.azure.com/{Organization}/{Project}/_apis/pipelines?api-version=7.0"
    
   #ReCreation of Pipeline for Existing YML File.
    repo_id = response_repoapi.json()['id']
    payload_pipelineapi = json.dumps({
        "configuration": {
            "path": Yaml_File,
            "repository": {
                "id": repo_id,
                "type": "azureReposGit"
                },
            "type": "yaml"
            },
        "name": Pipeline_Name                                   
        })
    
    requests.request("POST", url_pipelineapi, headers=headers_pipelineapi,data=payload_pipelineapi)
    
       
def main():
  
    # Credentials for User Authentication
    Organization = "ranjeet123"
    Project = "Demo"
    Repository = "Demo"
    Yaml_File = "azure-pipelines.yml"
    Pipeline_Name = "Sample_Pipeline"
    Personal_Access_Token = ""
    
    Authentication_ReCreation(Organization, Project, Repository, Yaml_File, Pipeline_Name, Personal_Access_Token)

   
if __name__ == "__main__":
    main()
    
    
    




