import subprocess
import os
import shutil
import requests
import json
import base64
import yaml
from jinja2 import Template, Environment, FileSystemLoader
import Auth_Creation_Module


def RenderTemp():
    
    # Load the JSON input
    with open('./DotNet_Main_Schema.json', 'r') as f:
        inputs = json.load(f)
        pipelineName = inputs["parameters"]["pipelineName"]["defaultValue"]
        ConfigurePipeline = inputs["parameters"]["ConfigurePipeline"]["defaultValue"]
        templateSelection = inputs["parameters"]["templateSelection"]["defaultValue"]
    

    if ConfigurePipeline == "Starter Pipeline":
        with open('./Variables_Jinja.json', 'r') as f:
            inputs = json.load(f)
            print("Input JSON loaded: ", inputs)
            
            env = Environment(loader=FileSystemLoader('./'))

    # Load the Jinja2 template
            template = env.get_template('./DotNet.j2')

    # Render the template using the JSON inputs
            yaml_content = template.render(inputs)
            print("Output of template.render function: ", yaml_content)

    # Write the rendered YAML content to a file
            with open('./final.yml', 'w') as f:
                f.write(yaml_content)
            with open('./final.yml', 'r') as f:
                yaml_content = f.read()
                print("Contents of final.yml: ", yaml_content)     

def PushRepo():
    az_repo_url = 'git clone https://dev.azure.com/ranjeet123/_git/Demo'                                
    result = subprocess.run(az_repo_url, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print("Cloning from AZ repo was successful")
        os.chdir("Demo")                                   # Change the current working directory to the cloned repositor
    else:
        print("Cloning from AZ repo failed with error:")
    if result.stderr is not None:
        print(result.stderr.decode("utf-8"))
    # move the file from the local file system to the repository

   
    local_file = 'C:\\Users\\RanjeetDhole\\Desktop\\MVP Pipeline\\yaml_template\DotNet\\final.yml'
   
    repo_file = 'final.yml'
    shutil.copy(local_file, repo_file)

    # Add the changes to the repository
    result = subprocess.run(["git", "add", repo_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print("Adding changes to the repository was successful")
    else:
        print("Adding changes to the repository failed with error:")
    if result.stderr is not None:
        print(result.stderr.decode("utf-8"))

    # Commit the changes
    result = subprocess.run(["git", "commit", "-m", "Test commit"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print("Committing changes was successful")
    else:
        print("Committing changes failed with error:")
    if result.stderr is not None:
        print(result.stderr.decode("utf-8"))

    result = subprocess.run(["git", "push"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)    #(git push )

    if result.returncode == 0:
        print("Pushing changes was successful")
    else:
        print("Pushing changes failed with error:")
    if result.stderr is not None:
        print(result.stderr.decode("utf-8"))    
        

def main():
    
    RenderTemp()
        
    Organization = "ranjeet123"
    Project = "Demo"
    Repository = "Demo"
    Yaml_File = "final.yml"
    Pipeline_Name = "final.yml"
    Personal_Access_Token = ""  

    PushRepo()
    
    Auth_Creation_Module.Authentication_PipelineCeation(Organization, Project, Repository, Yaml_File, Pipeline_Name, Personal_Access_Token)
   
if __name__ == "__main__":
    main()
    
