import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Generate sample dataset
np.random.seed(42)
data = pd.DataFrame({
    'feature1': np.random.rand(100),
    'feature2': np.random.rand(100),
    'target': np.random.choice([0, 1], 100)
})
data.to_csv('data.csv', index=False)

# Load dataset
data = pd.read_csv('data.csv')
X, y = data.drop(columns=['target']), data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train and evaluate SVM models
for kernel in ['linear', 'poly', 'rbf']:
    if kernel == 'poly':
        model = SVC(kernel=kernel, degree=3)
    else:
        model = SVC(kernel=kernel)
    model.fit(X_train, y_train)
    print(f'{kernel.capitalize()} SVM accuracy: {accuracy_score(y_test, model.predict(X_test)):.2f}')
