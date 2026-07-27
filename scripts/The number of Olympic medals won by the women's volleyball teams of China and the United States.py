import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 定义数据
data_usa = {
    'Year': [1964, 1968, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016],
    'medal_count': [0, 0, 12, 0, 12, 0, 0, 0, 12, 12, 12]
}
data_chn = {
    'Year': [1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016],
    'medal_count': [10, 11, 0, 9, 0, 12, 12, 0, 12]
}

# 创建DataFrame
usa_volleyball_usa_medal_count = pd.DataFrame(data_usa)
chn_volleyball_chn_medal_count = pd.DataFrame(data_chn)

def my_merge(df_A, df_B, v):
    # 合并两个DataFrame
    merged_df = pd.merge(df_A, df_B, on=['Year'], how='outer')
    merged_df.to_csv('中美两国奥运女子排球获奖牌数历年数据.csv', index=False)


    # 绘制图形
    plt.figure(figsize=(10, 6))
    plt.plot(merged_df['Year'], merged_df[v + '_x'], marker='D', label='usa_medal_count', color='SeaGreen', ls='-.')
    plt.plot(merged_df['Year'], merged_df[v + '_y'], marker='*', label='china_medal_count', color='r')
    plt.xticks(merged_df['Year'])  # 设置x轴刻度

    plt.legend()
    plt.xlabel('Year', fontname='Arial', fontsize=12)
    plt.ylabel(v, fontname='Arial', fontsize=12)
    plt.xticks(merged_df['Year'], fontname='Arial', fontsize=10)
    plt.yticks(fontname='Arial', fontsize=10)

    plt.grid()
    plt.savefig('中美两国奥运女子排球的奖牌数量.png')
    plt.show()
# 调用函数
my_merge(usa_volleyball_usa_medal_count[['Year', 'medal_count']], chn_volleyball_chn_medal_count[['Year', 'medal_count']], 'medal_count')