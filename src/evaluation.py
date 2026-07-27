from sklearn.metrics import (
    balanced_accuracy_score,
    accuracy_score,
    classification_report,
    confusion_matrix
)


def evaluate_model(y_true, y_pred):
    """
    Evaluate classification model performance.
    """

    print("=" * 60)
    print("Model Evaluation")
    print("=" * 60)

    print(f"Accuracy           : {accuracy_score(y_true, y_pred):.4f}")
    print(f"Balanced Accuracy  : {balanced_accuracy_score(y_true, y_pred):.4f}")

    print("\n" + "=" * 60)
    print("Classification Report")
    print("=" * 60)

    print(classification_report(y_true, y_pred))

    print("=" * 60)
    print("Confusion Matrix")
    print("=" * 60)

    print(confusion_matrix(y_true, y_pred))