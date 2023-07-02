# Import the necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Input data - X represents the independent variable and y represents the dependent variable
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Create an instance of the Linear Regression model
model = LinearRegression()

# Train the model using the input data
model.fit(X, y)

# Predict the output for a new input value
new_X = np.array([[6]])
predicted_y = model.predict(new_X)

# Calculate the error rate
mae = mean_absolute_error(y, model.predict(X))

# Visualize the data and the regression line
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.scatter(new_X, predicted_y, color='green', label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()

# Print the predicted output and error rate
print("Predicted y:", predicted_y)
print("Mean Absolute Error:", mae)
