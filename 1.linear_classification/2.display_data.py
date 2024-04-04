import pandas as pd
import matplotlib.pyplot as plt

# Load the random data
data = pd.read_excel('random_data.xlsx')

# Separate data by class
class_A = data[data['Label'] == 'Class_A']
class_B = data[data['Label'] == 'Class_B']

# Plot the data
plt.figure(figsize=(8, 6))
plt.scatter(class_A['Feature_1'], class_A['Feature_2'], color='blue', label='Class A')
plt.scatter(class_B['Feature_1'], class_B['Feature_2'], color='red', label='Class B')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Random Data')
plt.legend()
plt.grid(True)
plt.show()
