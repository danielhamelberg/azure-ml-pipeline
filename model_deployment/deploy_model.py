import os
from azureml.core import Workspace, Experiment, Environment, ScriptRunConfig, Model
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core.model import InferenceConfig

# Load the workspace from the saved config file
ws = Workspace.from_config()

# Define the model path
model_path = os.path.join(os.getenv("MODEL_DIR", "models"), "trained_model.pkl")

# Register the model
model = Model.register(workspace=ws,
                       model_path=model_path,
                       model_name="trained_model",
                       tags={"area": "classification", "type": "sklearn"},
                       description="A classification model")

# Define the environment
env = Environment.from_conda_specification(name="env", file_path="environment.yml")

# Define the inference configuration
inference_config = InferenceConfig(entry_script="score.py", environment=env)

# Define the deployment configuration
aci_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1, tags={"data": "classification"}, description="A classification model")

# Deploy the model
service_name = "classification-service"
service = Model.deploy(workspace=ws,
                       name=service_name,
                       models=[model],
                       inference_config=inference_config,
                       deployment_config=aci_config,
                       overwrite=True)

service.wait_for_deployment(show_output=True)

print(f"Service state: {service.state}")
print(f"Scoring URI: {service.scoring_uri}")