import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample dataset
np.random.seed(42)
df = pd.DataFrame({
    'feature1': np.random.rand(100) * 10,
    'feature2': np.random.rand(100) * 5,
    'feature3': np.random.rand(100) * 3,
    'target': np.random.rand(100) * 20
})
df.to_csv('dataset.csv', index=False)

# Load dataset
df = pd.read_csv('dataset.csv')
X, y = df[['feature1', 'feature2', 'feature3']], df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
reg = LinearRegression()
reg.fit(X_train, y_train)

# Predict and evaluate
y_pred = reg.predict(X_test)
print(f'Coefficients: {reg.coef_}')
print(f'Mean squared error: {mean_squared_error(y_test, y_pred):.2f}')
print(f'Coefficient of determination: {r2_score(y_test, y_pred):.2f}')

# Plot results
plt.scatter(X_test['feature1'], y_test, color='black', label='Actual')
plt.scatter(X_test['feature1'], y_pred, color='blue', label='Predicted')
plt.xlabel('Feature 1')
plt.ylabel('Target')
plt.legend()
plt.show()
