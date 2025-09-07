import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
heart_data = pd.read_csv('heart.csv')

# Splitting features and target variable
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

# Splitting data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Initializing Random Forest model with regularization
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,                # Limit tree depth
    min_samples_split=10,       # Require more samples to split
    max_leaf_nodes=20,          # Limit number of leaf nodes
    random_state=42
)

# Training the model
model.fit(X_train, Y_train)

# Accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy on Training data:', round(training_data_accuracy * 100, 2), "%")

# Accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test data:', round(test_data_accuracy * 100, 2), "%")

# Calculate & Print Total Accuracy
total_accuracy = (training_data_accuracy + test_data_accuracy) / 2
print('Total Accuracy:', round(total_accuracy * 100, 2), "%")

# Prediction on a sample input
input_data = (63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1)

# Convert input data to NumPy array and reshape
input_data_reshaped = np.asarray(input_data).reshape(1, -1)

# Make a prediction
prediction = model.predict(input_data_reshaped)

# Print the result
if prediction[0] == 0:
    print('The Person does not have a Heart Disease')
else:
    print('The Person has Heart Disease')
