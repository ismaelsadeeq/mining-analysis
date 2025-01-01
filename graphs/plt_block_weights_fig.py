import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Pool Name': [
        'Foundry USA', 'Binance Pool', 'MARA Pool', 'Luxor', 'AntPool', 'ViaBTC', 'Poolin', 
        'Braiins Pool', 'SBI Crypto', 'Ultimus Pool', 'BTC.com', 'SpiderPool', 'WhitePool', 
        'Ocean.xyz', 'EMCDPool', 'F2Pool', 'Pega Pool', 'Titan', 'KuCoin Pool', 'Terra Pool', 
        'CleanIncentive', '1THash', 'NiceHash', 'CKPool'
    ],
    'Avg. Block Weight': [
        3993030, 3993348, 3993017, 3993434, 3993554, 3993324, 3993308, 
        3993251, 3992911, 3993407, 3993399, 3993190, 3993072, 3988137, 
        3993273, 3997857, 3992894, 3992974, 3993282, 3993032, 3992946, 
        3993276, 3992987, 3993102
    ],
    'Min. Block Weight': [
        3992749, 3992753, 3992721, 3992782, 3992868, 3992881, 3992987, 
        3992695, 3992717, 3993076, 3992745, 3992912, 3992677, 3986489, 
        3993081, 3994044, 3992690, 3992926, 3993101, 3992863, 3992748, 
        3993085, 3992782, 3992897
    ],
    'Max. Block Weight': [
        3993523, 3993768, 3994944, 3993811, 3993918, 3993612, 3993613, 
        3993416, 3993047, 3993768, 3993781, 3993616, 3993631, 3990301, 
        3993428, 3998554, 3993018, 3993020, 3993504, 3993172, 3993038, 
        3993412, 3993148, 3993181
    ]
}

df_blocks = pd.DataFrame(data)

# Plotting the Line Plot
plt.figure(figsize=(14, 8))
plt.plot(df_blocks['Pool Name'], df_blocks['Avg. Block Weight'], marker='o', label='Avg. Block Weight', color='skyblue')
plt.plot(df_blocks['Pool Name'], df_blocks['Min. Block Weight'], marker='o', label='Min. Block Weight', color='lightgreen')
plt.plot(df_blocks['Pool Name'], df_blocks['Max. Block Weight'], marker='o', label='Max. Block Weight', color='salmon')

plt.title('Mining pools block weights', fontsize=16)
plt.xlabel('Pool Name', fontsize=14)
plt.ylabel('Weight (WU)', fontsize=14)
plt.xticks(rotation=90)

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Adjust layout to make room for the legend
plt.tight_layout()
plt.show()

