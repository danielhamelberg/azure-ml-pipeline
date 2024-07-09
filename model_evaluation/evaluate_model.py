# evaluate_model.py

import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score

def evaluate_model(y_true, y_pred, y_prob=None):
    """
    Evaluate the performance of a trained model using various metrics.
    
    Parameters:
    y_true (array-like): True labels.
    y_pred (array-like): Predicted labels.
    y_prob (array-like, optional): Predicted probabilities. Required for ROC AUC score.
    
    Returns:
    dict: Dictionary containing evaluation metrics.
    """
    metrics = {}
    
    # Accuracy
    metrics['accuracy'] = accuracy_score(y_true, y_pred)
    
    # Precision
    metrics['precision'] = precision_score(y_true, y_pred, average='weighted')
    
    # Recall
    metrics['recall'] = recall_score(y_true, y_pred, average='weighted')
    
    # F1 Score
    metrics['f1_score'] = f1_score(y_true, y_pred, average='weighted')
    
    # Confusion Matrix
    metrics['confusion_matrix'] = confusion_matrix(y_true, y_pred)
    
    # ROC AUC Score
    if y_prob is not None:
        metrics['roc_auc'] = roc_auc_score(y_true, y_prob, multi_class='ovr')
    
    return metrics

def print_evaluation_metrics(metrics):
    """
    Print the evaluation metrics in a readable format.
    
    Parameters:
    metrics (dict): Dictionary containing evaluation metrics.
    """
    print("Model Evaluation Metrics:")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall: {metrics['recall']:.4f}")
    print(f"F1 Score: {metrics['f1_score']:.4f}")
    print("Confusion Matrix:")
    print(metrics['confusion_matrix'])
    if 'roc_auc' in metrics:
        print(f"ROC AUC Score: {metrics['roc_auc']:.4f}")

# Example usage
if __name__ == "__main__":
    # Example true labels and predictions
    y_true = np.array([0, 1, 1, 0, 1, 0, 1, 1, 0, 0])
    y_pred = np.array([0, 1, 0, 0, 1, 0, 1, 1, 0, 1])
    y_prob = np.array([0.1, 0.9, 0.4, 0.2, 0.8, 0.3, 0.7, 0.9, 0.1, 0.6])
    
    metrics = evaluate_model(y_true, y_pred, y_prob)
    print_evaluation_metrics(metrics)