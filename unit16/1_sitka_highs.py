import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    
    # for index, colum_header in enumerate(header_row):
    #     print(index, colum_header)

    # 从文件种获取最高温度
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        highs.append(high)
        dates.append(current_date)
    

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# 设置图片的格式
ax.set_title("2018年7月每日最高温度", fontsize=24)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("温度(f)", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()