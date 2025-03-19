import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate sample classification dataset
np.random.seed(42)
data = pd.DataFrame({
    'feature1': np.random.randint(0, 10, 100),
    'feature2': np.random.randint(0, 5, 100),
    'target': np.random.choice([0, 1], 100)
})
data.to_csv('data.csv', index=False)

# Load dataset
data = pd.read_csv('data.csv')
X, y = data.drop(columns=['target']), data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree Classifier
dt = DecisionTreeClassifier().fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
print(f"Decision Tree Classifier Accuracy: {accuracy_score(y_test, y_pred_dt):.2f}")

# Random Forest Classifier
rf = RandomForestClassifier(n_estimators=10, random_state=42).fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print(f"Random Forest Classifier Accuracy: {accuracy_score(y_test, y_pred_rf):.2f}")
