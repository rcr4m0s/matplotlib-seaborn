import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. Dataset
data = {
    'Category': ['Tech', 'Tech', 'Fashion', 'Fashion', 'Home', 'Home'],
    'Store': ['Store A', 'Store B', 'Store A', 'Store B', 'Store A', 'Store B'],
    'Sales': [15000, 18000, 12000, 9000, 20000, 17000]
}
df = pd.DataFrame(data)

# 2. Seaborn Plot
sns.set_theme(style="whitegrid")
sns.barplot(data=df, x='Category', y='Sales', hue='Store')
plt.title('Sales Comparison by Store and Category')

# 3. Render
plt.show()