import os
import pandas as pd
from azureml.core import Workspace, Dataset, Datastore

def get_workspace(subscription_id, resource_group, workspace_name):
    return Workspace(subscription_id=subscription_id, resource_group=resource_group, workspace_name=workspace_name)

def register_datastore(workspace, datastore_name, account_name, container_name, account_key):
    datastore = Datastore.register_azure_blob_container(workspace=workspace,
                                                        datastore_name=datastore_name,
                                                        container_name=container_name,
                                                        account_name=account_name,
                                                        account_key=account_key)
    return datastore

def upload_data_to_datastore(datastore, src_dir, target_path):
    datastore.upload(src_dir=src_dir, target_path=target_path, overwrite=True)

def create_dataset_from_datastore(workspace, datastore_name, dataset_name, file_path):
    datastore = Datastore.get(workspace, datastore_name)
    dataset = Dataset.Tabular.from_delimited_files(path=(datastore, file_path))
    dataset = dataset.register(workspace=workspace, name=dataset_name, create_new_version=True)
    return dataset

def main():
    subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
    resource_group = os.getenv('AZURE_RESOURCE_GROUP')
    workspace_name = os.getenv('AZURE_WORKSPACE_NAME')
    datastore_name = os.getenv('AZURE_DATASTORE_NAME')
    account_name = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
    container_name = os.getenv('AZURE_BLOB_CONTAINER_NAME')
    account_key = os.getenv('AZURE_STORAGE_ACCOUNT_KEY')
    src_dir = os.getenv('DATA_SOURCE_DIRECTORY')
    target_path = os.getenv('DATA_TARGET_PATH')
    dataset_name = os.getenv('AZURE_DATASET_NAME')
    file_path = os.getenv('DATA_FILE_PATH')

    workspace = get_workspace(subscription_id, resource_group, workspace_name)
    datastore = register_datastore(workspace, datastore_name, account_name, container_name, account_key)
    upload_data_to_datastore(datastore, src_dir, target_path)
    dataset = create_dataset_from_datastore(workspace, datastore_name, dataset_name, file_path)
    print(f"Dataset {dataset_name} registered successfully.")

if __name__ == "__main__":
    main()