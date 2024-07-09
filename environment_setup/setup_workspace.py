import os
from azureml.core import Workspace
from azureml.core.authentication import InteractiveLoginAuthentication

def create_workspace(subscription_id, resource_group, workspace_name, region):
    interactive_auth = InteractiveLoginAuthentication()
    
    try:
        ws = Workspace(subscription_id=subscription_id,
                       resource_group=resource_group,
                       workspace_name=workspace_name,
                       auth=interactive_auth)
        print("Workspace already exists. Using the existing workspace.")
    except:
        ws = Workspace.create(name=workspace_name,
                              subscription_id=subscription_id,
                              resource_group=resource_group,
                              location=region,
                              create_resource_group=True,
                              auth=interactive_auth)
        print("Workspace created successfully.")
    
    ws.write_config(path=".azureml")
    return ws

if __name__ == "__main__":
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    resource_group = os.getenv("AZURE_RESOURCE_GROUP")
    workspace_name = os.getenv("AZURE_WORKSPACE_NAME")
    region = os.getenv("AZURE_REGION")

    if not all([subscription_id, resource_group, workspace_name, region]):
        raise ValueError("Please set the environment variables: AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP, AZURE_WORKSPACE_NAME, AZURE_REGION")

    create_workspace(subscription_id, resource_group, workspace_name, region)