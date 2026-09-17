import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load built-in dataset
iris = sns.load_dataset('iris')

# 2. Compute correlation matrix for numeric columns
numeric_df = iris.drop(columns=['species'])
correlation_matrix = numeric_df.corr()

# 3. Create Heatmap
sns.set_theme(style="white")
sns.heatmap(
    correlation_matrix, 
    annot=True,       # Displays numerical correlation values inside boxes
    cmap='coolwarm',  # Color palette (blue = low/negative, red = high/positive)
    fmt='.2f'         # Format numbers to 2 decimal places
)

# 4. Customization
plt.title('Correlation Heatmap of Iris Dataset Features')

# 5. Display
plt.show()