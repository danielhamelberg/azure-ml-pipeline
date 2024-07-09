import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Define paths
data_path = 'data/dataset.csv'
model_path = 'models/random_forest_model.pkl'
scaler_path = 'models/scaler.pkl'

# Load dataset
def load_data(path):
    return pd.read_csv(path)

# Preprocess data
def preprocess_data(df):
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test, scaler

# Train model
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Evaluate model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)

# Save model and scaler
def save_artifacts(model, scaler, model_path, scaler_path):
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

# Main function
def main():
    # Load data
    df = load_data(data_path)
    
    # Preprocess data
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Evaluate model
    accuracy = evaluate_model(model, X_test, y_test)
    print(f'Model Accuracy: {accuracy}')
    
    # Save model and scaler
    save_artifacts(model, scaler, model_path, scaler_path)

if __name__ == '__main__':
    main()