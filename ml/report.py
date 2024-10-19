import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

def parse_latex_table(latex_str):
    # Use regex to extract numbers from the LaTeX table
    numbers = re.findall(r'\d+', latex_str)
    # Convert to a numpy array and reshape it
    numbers = np.array(numbers, dtype=int)
    # Determine the shape of the confusion matrix
    num_classes = int(np.sqrt(len(numbers)))  # Assuming it's a square matrix for simplicity
    return numbers.reshape((num_classes, num_classes))

def plot_normalized_confusion_matrix(confusion_matrix):
    # Normalize the confusion matrix by row (i.e., by true label)
    row_sums = confusion_matrix.sum(axis=1, keepdims=True)
    normalized_matrix = confusion_matrix / row_sums
    # Plot the normalized confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(normalized_matrix, annot=True, fmt='.2%', cmap='Blues', cbar=True,
                xticklabels=np.arange(normalized_matrix.shape[1]),
                yticklabels=np.arange(normalized_matrix.shape[0]))
    plt.title('Normalized Confusion Matrix')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()

# Example usage
latex_str_1 = r"\begin{tabular}[c]{@{}c@{}}[[3905    1]\\ {[}  10 2266{]}]\end{tabular}"
# latex_str_2 = r"\begin{tabular}[c]{@{}c@{}}[[3561  927  663]\\ {[}   3 2273    0{]}\\{[}   2    1 1472{]}]\end{tabular}"

# Parse the LaTeX string to get the confusion matrix
confusion_matrix_1 = parse_latex_table(latex_str_1)
# confusion_matrix_2 = parse_latex_table(latex_str_2)

# Plot normalized confusion matrices
plot_normalized_confusion_matrix(confusion_matrix_1)
# plot_normalized_confusion_matrix(confusion_matrix_2)
