# import numpy as np

# data = np.array([1, 2, 2, 3, 4, 6, 8, 9, 10, 100])

# mean = np.mean(data)
# std_dev = np.std(data)

# # Set a threshold (e.g., 3 standard deviations)
# threshold = 3

# # Identify outliers
# outliers = (data - mean) / std_dev > threshold

# print("Outliers:", data[outliers])

import numpy as np
from scipy.stats import zscore

data = np.array([1, 2, 2, 3, 4, 6, 8, 9, 10, 100])

z_scores = zscore(data)
threshold = 3

# Identify outliers
outliers = np.abs(z_scores) > threshold

print("Outliers:", data[outliers])

# import numpy as np

# # Example data with outliers
# data = np.array([1, 2, 3, 4, 5, 6, 200, 8, 9, 100])

# # Calculate Q1 and Q3
# Q1 = np.percentile(data, 25)
# Q3 = np.percentile(data, 75)

# # Calculate IQR
# IQR = Q3 - Q1

# # Identify outliers based on IQR
# outliers = (data < Q1 - 1.5 * IQR) | (data > Q3 + 1.5 * IQR)

# # View the values and indices of outliers
# print("Values of outliers:", data[outliers])
# print("Indices of outliers:", np.where(outliers)[0])



