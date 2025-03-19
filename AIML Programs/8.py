from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Load dataset & split
X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define models
models = [
    ('svm', SVC(kernel='linear', probability=True)),
    ('rf', RandomForestClassifier(n_estimators=10)),
    ('lr', LogisticRegression(max_iter=200))
]

# Ensemble model
ensemble = VotingClassifier(estimators=models, voting='soft').fit(X_train, y_train)

# Evaluate
print("Ensemble Accuracy:", round(ensemble.score(X_test, y_test), 2))
