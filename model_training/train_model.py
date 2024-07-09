import os
import joblib
import pandas as pd
from azureml.core import Workspace, Experiment, Run
from azureml.train.automl import AutoMLConfig
from azureml.core.dataset import Dataset

# Load the workspace from the saved config file
ws = Workspace.from_config()

# Define the experiment name
experiment_name = 'automl-classification'
experiment = Experiment(ws, experiment_name)

# Load the preprocessed data
data_path = os.path.join('data', 'preprocessed_data.csv')
data = pd.read_csv(data_path)

# Convert the data to an Azure ML Dataset
dataset = Dataset.Tabular.from_delimited_files(path=[data_path])

# Define the target column
target_column_name = 'target'

# Configure AutoML settings
automl_settings = {
    "iteration_timeout_minutes": 10,
    "experiment_timeout_hours": 1,
    "n_cross_validations": 5,
    "primary_metric": 'accuracy',
    "verbosity": logging.INFO,
    "enable_early_stopping": True
}

# Configure AutoML
automl_config = AutoMLConfig(
    task='classification',
    training_data=dataset,
    label_column_name=target_column_name,
    **automl_settings
)

# Submit the AutoML run
run = experiment.submit(automl_config, show_output=True)

# Get the best model
best_run, fitted_model = run.get_output()

# Save the best model
model_path = os.path.join('outputs', 'best_model.pkl')
joblib.dump(fitted_model, model_path)

print(f"Best model saved to {model_path}")