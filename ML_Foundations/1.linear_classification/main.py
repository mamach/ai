import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the random data
data = pd.read_excel('random_data.xlsx')

# Split the data into features (X) and labels (y)
X = data[['Feature_1', 'Feature_2']]
y = data['Label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Print the model parameters (coefficients)
print("Model Parameters (Coefficients):")
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)


# Predict the labels for the test set
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
