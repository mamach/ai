import pandas as pd
import numpy as np

# Generate random data
# np.random.seed(0)
num_samples = 10000
data = pd.DataFrame({
    'Feature_1': np.random.randint(0, 100, num_samples),
    'Feature_2': np.random.randint(0, 100, num_samples),
    'Label': np.random.choice(['Class_A', 'Class_B'], num_samples)
})

# Save data to Excel
data.to_excel('random_data.xlsx', index=False)

print("Random data saved to 'random_data.xlsx'.")
