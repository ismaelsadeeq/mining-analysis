import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Corrected Data for pools generating blocks with Coinbase Weight > 4000 WU
data_coinbase = {
    'Pool Name': [
        'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 
        'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 
        'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 'unknown pool/miner', 
        'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 'unknown pool/miner', 
        'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 
        'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz', 'Ocean.xyz'
    ],
    'Coinbase Weight': [
        8352, 5892, 7032, 5760, 6140, 6732, 5560, 7688, 5308, 8080, 
        6892, 5964, 7160, 5868, 7000, 6920, 7212, 6964, 7460, 7864, 
        7516, 7404, 6412, 7504, 9272, 8452, 8424, 6536, 6456, 6888
    ]
}

df_coinbase = pd.DataFrame(data_coinbase)

# Plotting the Box Plot
plt.figure(figsize=(12, 8))
sns.boxplot(x='Pool Name', y='Coinbase Weight', data=df_coinbase)
plt.title('Distribution of Coinbase Transaction Weights')
plt.xlabel('Pool Name')
plt.ylabel('Coinbase Weight (WU)')

# Highlight the min, max, and average
min_weight = df_coinbase['Coinbase Weight'].min()
max_weight = df_coinbase['Coinbase Weight'].max()
avg_weight = df_coinbase['Coinbase Weight'].mean()

plt.axhline(min_weight, color='blue', linestyle='--', label=f'Min Weight: {min_weight} WU')
plt.axhline(max_weight, color='red', linestyle='--', label=f'Max Weight: {max_weight} WU')
plt.axhline(avg_weight, color='green', linestyle='--', label=f'Avg Weight: {avg_weight:.2f} WU')

# Place the legend outside the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()