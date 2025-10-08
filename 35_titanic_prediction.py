# titanic_prediction.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Combine train and test for preprocessing
combine = [train_data, test_data]

# Feature Engineering
for dataset in combine:
    # Fill missing Age with median
    dataset['Age'].fillna(dataset['Age'].median(), inplace=True)
    
    # Fill Embarked with mode
    dataset['Embarked'].fillna(dataset['Embarked'].mode()[0], inplace=True)
    
    # Fill Fare in test set
    dataset['Fare'].fillna(dataset['Fare'].median(), inplace=True)
    
    # Convert Sex to numeric
    dataset['Sex'] = dataset['Sex'].map({'male': 0, 'female': 1}).astype(int)
    
    # Convert Embarked to numeric
    dataset['Embarked'] = dataset['Embarked'].map({'S': 0, 'C': 1, 'Q': 2}).astype(int)
    
    # Create new feature FamilySize
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1

# Drop features we won't use
train_data = train_data.drop(['Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1)
test_passenger_ids = test_data['PassengerId']  # Keep for submission
test_data = test_data.drop(['Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1)

# Split features and target
X = train_data.drop('Survived', axis=1)
y = train_data['Survived']

# Train/Test Split for validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Validation
y_pred_val = model.predict(X_val)
print("Validation Accuracy:", accuracy_score(y_val, y_pred_val))

# Predict on test data
predictions = model.predict(test_data)

# Save submission
submission = pd.DataFrame({
    'PassengerId': test_passenger_ids,
    'Survived': predictions
})

submission.to_csv('titanic_submission.csv', index=False)
print("Submission file saved as titanic_submission.csv")
