import numpy as np
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator
from pgmpy.inference import VariableElimination
import os

# Check if the dataset already exists
if not os.path.exists('heart.csv'):
    np.random.seed(42)

    # Generate static dataset with more entries for age=28 and chol=100
    data = {
        'age': np.concatenate([np.random.randint(20, 80, 990), np.full(10, 28)]),
        'sex': np.random.randint(0, 2, 1000),
        'trestbps': np.random.randint(100, 180, 1000),
        'chol': np.concatenate([np.random.randint(150, 300, 990), np.full(10, 100)]),
        'fbs': np.random.randint(0, 2, 1000),
        'restecg': np.random.randint(0, 2, 1000),
        'thalach': np.random.randint(100, 200, 1000),
        'exang': np.random.randint(0, 2, 1000),
        'heartdisease': np.random.randint(0, 5, 1000)
    }

    static_df = pd.DataFrame(data)
    static_df.to_csv('heart.csv', index=False)

# Read static dataset
heartDisease = pd.read_csv('heart.csv')

# Display the dataset
print('Few examples from the dataset:')
print(heartDisease.head())

# Model Bayesian Network
Model = BayesianModel([
    ('age', 'trestbps'), ('age', 'fbs'),
    ('sex', 'trestbps'), ('exang', 'trestbps'),
    ('trestbps', 'heartdisease'), ('fbs', 'heartdisease'),
    ('heartdisease', 'restecg'),
    ('heartdisease', 'thalach'),
    ('heartdisease', 'chol')
])

# Learning CPDs using Bayesian Estimator with pseudocounts
print('\nLearning CPD using Bayesian Estimator')
Model.fit(heartDisease, estimator=BayesianEstimator, prior_type='BDeu', equivalent_sample_size=10)

# Inferencing with Bayesian Network
print('\nInferencing with Bayesian Network:')
HeartDisease_infer = VariableElimination(Model)

# Compute Probability of HeartDisease given Age=28
print('\n1. Probability of HeartDisease given Age=28')
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': 28})
print(q)

# Compute Probability of HeartDisease given Cholesterol=100
print('\n2. Probability of HeartDisease given Cholesterol=100')
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'chol': 100})
print(q)
