# -*- coding: utf-8 -*-
"""knn_final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u6AlT1WZ-pRLumu-Wv9H1x8RxgwIk5a9
"""

import numpy as np
import pandas as pd
df = pd.read_csv('sat.csv')
df

df.info()

# Assuming the class variable is named "label"
print(df.columns)

plt.figure(figsize=(6, 4))
sns.countplot(x='label', data=df)
plt.title("Distribution of label")
plt.show()

X = df.drop("label", axis=1)
y = df["label"]

print(X.head())

print(df.describe())

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(X)

# Create a new DataFrame with scaled values
scaled_X = pd.DataFrame(scaled_data, columns=X.columns)

statistics = scaled_X.describe()
print(statistics)

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(scaled_X, y, test_size=0.2, random_state=43)

# Print the shapes of the resulting sets
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

from sklearn.neighbors import KNeighborsClassifier

#Instantiate a default KNN model
default_knn = KNeighborsClassifier()

#Train the default model using the training data
clf = default_knn.fit(X_train, y_train)

#Calculate predictions on the testing data
y_pred_default = clf.predict(X_test)

# Display the first few predictions
y_pred_default[:5]

# Print the parameters of the default KNN model
print("Parameters of the Default KNN Model:")
print(clf.get_params())

predicted = clf.predict(X_test)
print(predicted .shape)

from sklearn.metrics import multilabel_confusion_matrix, classification_report

# Obtain the multilabel confusion matrix
multilabel_confusion_mat = multilabel_confusion_matrix(y_test, predicted)

# Print the multilabel confusion matrix
print("Multilabel Confusion Matrix:")
print(multilabel_confusion_mat)

report_default = classification_report(y_test, y_pred_default)
print("Classification Report (Default KNN):")
print(report_default)

import seaborn as sns
import matplotlib.pyplot as plt

# Plot each individual confusion matrix as a heatmap
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

for i, ax in enumerate(axes.flatten()):
    sns.heatmap(multilabel_confusion_mat[i], annot=True, cmap='Blues', ax=ax)
    ax.set_title(f'Confusion Matrix Class {i}')
    ax.set_xlabel('Predicted')
    ax.set_ylabel('True')

plt.tight_layout()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Compute the correlation matrix
correlation_matrix = scaled_X.corr()

# Plot the correlation matrix heatmap
plt.figure(figsize=(20, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Compute the correlation between features and class variable
feature_correlation = df.corr()['label'].drop('label')

# Plot the correlation values on a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_correlation.index, y=feature_correlation.values)
plt.xticks(rotation=90)
plt.xlabel('Features')
plt.ylabel('Correlation')
plt.title('Correlation between Features and Class Variable')
plt.show()

"""weighted knn"""

from sklearn.neighbors import DistanceMetric

# Instantiate a randomly "weighted" KNN model
# Generate random weights for each feature
random_weights = np.random.random(X_train.shape[1])

# Define a custom distance metric using the random weights
def weighted_manhattan_distance(x, y):
    return np.sum(np.abs(x - y) * random_weights)

# Instantiate the weighted KNN model with the custom distance metric
weighted_knn = KNeighborsClassifier(metric=weighted_manhattan_distance)

# Observe the parameters of the "weighted" KNN model
print(weighted_knn.get_params())

print(random_weights.shape)

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(scaled_X, y, test_size=0.2, random_state=43)

# Print the shapes of the resulting sets
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

from sklearn.neighbors import KNeighborsClassifier

# Step 14: Train the default model using the training data
clf = weighted_knn.fit(X_train, y_train)

# Step 15: Calculate predictions on the testing data
pred_weighted = clf.predict(X_test)

# Display the first few predictions
print(pred_weighted[:5])

import seaborn as sns
import matplotlib.pyplot as plt

# Plot each individual confusion matrix as a heatmap
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

for i, ax in enumerate(axes.flatten()):
    sns.heatmap(multilabel_confusion_mat[i], annot=True, cmap='Blues', ax=ax)
    ax.set_title(f'Confusion Matrix Class {i}')
    ax.set_xlabel('Predicted')
    ax.set_ylabel('True')

plt.tight_layout()
plt.show()

from sklearn.metrics import multilabel_confusion_matrix, classification_report

# Obtain the multilabel confusion matrix
multilabel_confusion_mat_w = multilabel_confusion_matrix(y_test, pred_weighted)

# Print the multilabel confusion matrix
print("Multilabel Confusion Matrix:")
print(multilabel_confusion_mat_w)

# Print the classification report
report_weighted = classification_report(y_test, pred_weighted)
print("Classification Report (Weighted KNN):")
print(report_weighted)

import seaborn as sns
import matplotlib.pyplot as plt

# Compute the correlation matrix
correlation_matrix = scaled_X.corr()

# Plot the correlation matrix heatmap
plt.figure(figsize=(20, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()
# Compute the correlation between features and class variable
feature_correlation = df.corr()['label'].drop('label')

import seaborn as sns
import matplotlib.pyplot as plt

# Plot the correlation values on a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_correlation.index, y=feature_correlation.values)
plt.xticks(rotation=90)
plt.xlabel('Features')
plt.ylabel('Correlation')
plt.title('Correlation between Features and Class Variable')
plt.show()

# Step 28: Perform K-fold cross-validation to find the optimum value of k
from sklearn.model_selection import cross_val_score

k_values = list(range(1, 31))
accuracy_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
    accuracy_scores.append(scores.mean())

# Step 29: Create a plot of the accuracy scores versus the k values
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracy_scores, marker='o')
plt.title("Accuracy vs. K Value")
plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.xticks(k_values)
plt.grid(True)
plt.show()

optimal_k = k_values[np.argmax(accuracy_scores)]
print(f"Optimum K: {optimal_k}")

# Step 30: Instantiate an "optimum" KNN model
optimal_knn = KNeighborsClassifier(n_neighbors=optimal_k)

# Step 31: Train the "optimum" model using the training data
optimal_knn.fit(X_train, y_train)

# Step 32: Calculate predictions on the testing data
y_pred_optimal = optimal_knn.predict(X_test)

import seaborn as sns
import matplotlib.pyplot as plt

# Plot each individual confusion matrix as a heatmap
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

for i, ax in enumerate(axes.flatten()):
    sns.heatmap(multilabel_confusion_mat[i], annot=True, cmap='Blues', ax=ax)
    ax.set_title(f'Confusion Matrix Class {i}')
    ax.set_xlabel('Predicted')
    ax.set_ylabel('True')

plt.tight_layout()
plt.show()

# Step 34: Print the classification report
class_report_optimal = classification_report(y_test, y_pred_optimal)
print(class_report_optimal)

# Step 35: Compare the results with previous models

print("\nClassification Report for Default KNN Model:")
print(report_default)

print("\nClassification Report for Weighted KNN Model:")
print(report_weighted)

print("\nClassification Report for Optimum KNN Model:")
print(class_report_optimal )

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Replace 'your_dataset.csv' with the actual file path to your dataset
dataset_path = 'sat.csv'

# Load your dataset into a Pandas DataFrame
data = pd.read_csv(dataset_path)

# Assuming 'data' is your Pandas DataFrame with numerical columns to be standardized
numerical_columns = data.select_dtypes(include=['float64', 'int64'])  # Select numerical columns
scaler = StandardScaler()
data_std = scaler.fit_transform(numerical_columns)

# If your dataset has a label column, you can separate it like this:
X = data.drop('label', axis=1)  # Drop the label column
y = data['label']  # This is your label column

# Apply PCA to reduce dimensionality
pca = PCA(n_components=2)  # Choose the number of components (2 for 2D visualization)
data_pca = pca.fit_transform(data_std)

# Create a scatter plot for visualization
plt.figure(figsize=(10, 8))
plt.scatter(data_pca[:, 0], data_pca[:, 1], c=y, cmap='viridis')
plt.title('Statlog (Landsat Satellite) Dataset Visualization (PCA)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(label='Class Labels')
plt.show()