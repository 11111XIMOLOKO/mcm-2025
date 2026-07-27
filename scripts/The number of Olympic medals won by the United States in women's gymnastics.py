import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 定义数据
data_chn = {
    'Year': [1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1984, 1984, 1988, 1988, 1992, 1992, 1996, 1996, 2000, 2004, 2004, 2008, 2012, 2012, 2016, 2016],
    'Gold_count': [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 8, 0, 0, 1, 0, 2, 7, 0, 8, 0]
}

# 创建DataFrame
Volleyball_china_medal_count = pd.DataFrame(data_chn)

def draw_curve(df, Year, value):
    df['change rate'] = df[value].pct_change()  # 计算百分比变化
    df['diff'] = df[value].diff()  # 计算绝对diff

    # 设置阈值来识别突增
    threshold = 0.2
    sudden_increase = df[(df['change rate'] > threshold) | (df['diff'] > 5)]  # 绝对diff大于5

    print(sudden_increase[[Year, value, 'change rate', 'diff']])

    plt.figure(figsize=(18, 10))
    plt.plot(df[Year], df[value], marker='d', label=value, color='xkcd:salmon')
    plt.scatter(sudden_increase[Year], sudden_increase[value], color='xkcd:dark pink', label='surge', zorder=5)
    plt.xlabel(Year, fontname='Arial', fontsize=12)
    plt.ylabel(value, fontname='Arial', fontsize=12)
    plt.xticks(fontname='Arial', fontsize=10)
    plt.yticks(fontname='Arial', fontsize=10)

    plt.legend()
    plt.grid()
    plt.savefig('The number of Olympic medals won by the United States in women\'s gymnastics.png')
    plt.show()

# 调用函数
draw_curve(Volleyball_china_medal_count, 'Year', 'Gold_count')