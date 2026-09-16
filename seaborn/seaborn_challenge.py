import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load built-in dataset
tips = sns.load_dataset('tips')

# 2. Set theme
sns.set_theme(style="whitegrid")

# 3. Create Boxplot
sns.boxplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='sex'
)

# 4. Customization
plt.title('Total Bill Distribution by Day and Gender')

# 5. Display
plt.show()