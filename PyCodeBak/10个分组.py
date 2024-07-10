import pandas as pd

# 读取Excel文件
# 将 'your_file.xlsx' 替换为您的文件名
df = pd.read_excel('temu.xlsx', sheet_name='Sheet1')

# 准备一个新列来存放分组后的数据
df['Grouped'] = ''

# 分组并将结果放入新列
for i in range(0, len(df), 12):
    group = df.iloc[i:i+12, 0].tolist()
    df.at[i+11, 'Grouped'] = ', '.join(group)

# 保存更改到新的Excel文件
# 将 'output_file.xlsx' 替换为您希望保存的文件名
df.to_excel('output_file.xlsx', index=False)
