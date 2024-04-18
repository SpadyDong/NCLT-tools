import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
df = pd.read_csv("D:/groundtruth_2012-01-08.csv")

# 提取第二列和第三列作为 x 和 y 数据
x = df.iloc[:, 1]  # 第二列
y = df.iloc[:, 2]  # 第三列

# 设置点的大小
point_size = 3

plt.scatter(x, y, s=point_size, marker='o', color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('NCLT')
plt.show()
