import pandas as pd
import pickle
import argparse
import random

seed = 123
random.seed(seed)

# 设定文件路径
input_file = '/Users/juny811/PycharmProjects/pythonProject/atlantic_new.csv'  # 替换为你的文件路径

# 读取 CSV 文件
data = pd.read_csv(input_file)

# 将 Date 列转换为 datetime 格式
data['datetime'] = pd.to_datetime(data['Date'], format='%Y%m%d')  # 按 YYYYMMDD 格式解析日期

# 按时间分组：设定时间区间
time_interval_days = 21  # 例如按 3 周（21 天）分组
data['time_group'] = data['datetime'].dt.floor(f'{time_interval_days}D')

# 选择需要的列
filtered_data = data[['time_group', 'Maximum Wind', 'Longitude', 'Latitude']]

# 分组并生成三层列表
grouped_list = [
    sorted(group[['Maximum Wind', 'Longitude', 'Latitude']].values.tolist())
    for _, group in filtered_data.groupby('time_group')
]

# 随机化数据
random.shuffle(grouped_list)

# 分割训练、测试和验证集
test_val_len = int(len(grouped_list) * 0.05)
test_data = [grouped_list.pop() for _ in range(test_val_len)]
val_data = [grouped_list.pop() for _ in range(test_val_len)]

# 保存为 .pkl 文件
with open("/Users/juny811/PycharmProjects/pythonProject/data_train.pkl", "wb") as f:
    pickle.dump(grouped_list, f)
with open("/Users/juny811/PycharmProjects/pythonProject/data_test.pkl", "wb") as f:
    pickle.dump(test_data, f)
with open("/Users/juny811/PycharmProjects/pythonProject/data_val.pkl", "wb") as f:
    pickle.dump(val_data, f)

print(f"数据转换完成：训练集 {len(grouped_list)}，测试集 {len(test_data)}，验证集 {len(val_data)}")