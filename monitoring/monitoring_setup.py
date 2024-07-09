import logging
from azureml.core import Workspace, Experiment, Run
from azureml.core.model import Model
from azureml.telemetry import set_diagnostics_collection

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_workspace(subscription_id, resource_group, workspace_name):
    try:
        ws = Workspace(subscription_id=subscription_id, resource_group=resource_group, workspace_name=workspace_name)
        logger.info("Workspace loaded successfully.")
    except Exception as e:
        logger.error(f"Failed to load workspace: {e}")
        raise
    return ws

def setup_experiment(workspace, experiment_name):
    try:
        experiment = Experiment(workspace=workspace, name=experiment_name)
        logger.info("Experiment created successfully.")
    except Exception as e:
        logger.error(f"Failed to create experiment: {e}")
        raise
    return experiment

def log_run_details(run):
    try:
        logger.info(f"Run ID: {run.id}")
        logger.info(f"Run Status: {run.status}")
        logger.info(f"Run Metrics: {run.get_metrics()}")
    except Exception as e:
        logger.error(f"Failed to log run details: {e}")
        raise

def setup_model_monitoring(workspace, model_name):
    try:
        model = Model(workspace, name=model_name)
        logger.info(f"Model {model_name} loaded successfully.")
        logger.info(f"Model ID: {model.id}")
        logger.info(f"Model Version: {model.version}")
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        raise

def enable_diagnostics():
    try:
        set_diagnostics_collection(send_diagnostics=True)
        logger.info("Diagnostics collection enabled.")
    except Exception as e:
        logger.error(f"Failed to enable diagnostics collection: {e}")
        raise

if __name__ == "__main__":
    subscription_id = "your-subscription-id"
    resource_group = "your-resource-group"
    workspace_name = "your-workspace-name"
    experiment_name = "your-experiment-name"
    model_name = "your-model-name"

    ws = setup_workspace(subscription_id, resource_group, workspace_name)
    experiment = setup_experiment(ws, experiment_name)
    enable_diagnostics()

    # Example run logging
    run = Run(experiment=experiment, run_id="your-run-id")
    log_run_details(run)

    # Example model monitoring
    setup_model_monitoring(ws, model_name)