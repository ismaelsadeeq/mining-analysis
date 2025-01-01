import matplotlib.pyplot as plt
import pandas as pd

data_coinbase_weights = {
    'Pool Name': [
        'Ocean.xyz', 'Unknown pool', 'Foundry USA', 'Binance Pool', 'MARA Pool', 'Luxor', 
        'AntPool', 'ViaBTC', 'Poolin', 'Braiins Pool', 'SBI Crypto', 'Ultimus Pool', 
        'BTC.com', 'SpiderPool', 'WhitePool', 'EMCDPool', 'F2Pool', 'Pega Pool', 
        'Titan', 'KuCoin Pool', 'Terra Pool', 'CleanIncentive', '1THash', 'NiceHash', 'CKPool'
    ],
    'Avg. Coinbase Weight': [
        6994, 7432, 748, 748, 720, 780, 732, 880, 904, 684, 716, 1056, 740, 892, 676, 1080, 
        1724, 688, 696, 1092, 844, 728, 1084, 780, 856
    ],
    'Min. Coinbase Weight': [
        5308, 7000, 748, 748, 720, 780, 732, 880, 904, 684, 716, 1056, 740, 892, 676, 1080, 
        1724, 688, 696, 1092, 844, 728, 1084, 780, 856
    ],
    'Max. Coinbase Weight': [
        9272, 7864, 1192, 1440, 904, 1480, 1612, 1284, 1336, 1124, 716, 1440, 1472, 1288, 
        1304, 1304, 1364, 688, 696, 1316, 844, 728, 1084, 820, 856
    ]
}

# Convert the data to a DataFrame
df_coinbase_weights = pd.DataFrame(data_coinbase_weights)

# Plotting the Line Plot
plt.figure(figsize=(14, 8))
plt.plot(df_coinbase_weights['Pool Name'], df_coinbase_weights['Avg. Coinbase Weight'], marker='o', label='Avg. Coinbase Weight', color='skyblue')
plt.plot(df_coinbase_weights['Pool Name'], df_coinbase_weights['Min. Coinbase Weight'], marker='o', label='Min. Coinbase Weight', color='lightgreen')
plt.plot(df_coinbase_weights['Pool Name'], df_coinbase_weights['Max. Coinbase Weight'], marker='o', label='Max. Coinbase Weight', color='salmon')
plt.title('Coinbase Transaction Weights for Pools', fontsize=16)
plt.xlabel('Pool Name', fontsize=14)
plt.ylabel('Weight (WU)', fontsize=14)
plt.xticks(rotation=90)

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Adjust layout to make room for the legend
plt.tight_layout()
plt.show()