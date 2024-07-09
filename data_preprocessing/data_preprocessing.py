import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def handle_missing_values(data):
    data = data.fillna(method='ffill')
    return data

def encode_categorical_columns(data):
    label_encoders = {}
    for column in data.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le
    return data, label_encoders

def scale_features(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data, scaler

def split_data(data, target_column, test_size=0.2, random_state=42):
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def preprocess_data(file_path, target_column):
    data = load_data(file_path)
    data = handle_missing_values(data)
    data, label_encoders = encode_categorical_columns(data)
    scaled_data, scaler = scale_features(data)
    X_train, X_test, y_train, y_test = split_data(scaled_data, target_column)
    return X_train, X_test, y_train, y_test, label_encoders, scaler

if __name__ == "__main__":
    file_path = "path_to_your_data.csv"
    target_column = "target"
    X_train, X_test, y_train, y_test, label_encoders, scaler = preprocess_data(file_path, target_column)
    print("Data preprocessing completed.")