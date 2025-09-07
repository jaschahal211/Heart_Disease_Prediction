# Importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset (assumes dataset is a CSV file)
# Replace 'heart_disease.csv' with your dataset file path
df = pd.read_csv('heart.csv')

# Display the first few rows of the dataset to understand its structure
print(df.head())

# Preprocessing the data: Assuming the last column is the target
X = df.iloc[:, :-1]  # Features (all columns except the last one)
y = df.iloc[:, -1]   # Target (last column)

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling: KNN performs better with scaled data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create KNN model with 5 neighbors (this can be tuned)
knn = KNeighborsClassifier(n_neighbors=5)

# Train the model
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Output the accuracy score
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("THe accuracy model that models are dependent ")