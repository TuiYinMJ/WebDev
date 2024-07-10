import os
import pandas as pd

# 定义三个查找路径
search_paths = {
    '彩页': r'C:\Users\Administrator\Nutstore\1\义乌市植美工艺品\彩页',
    '96x64不干胶': r'C:\Users\Administrator\Nutstore\1\义乌市植美工艺品\不干胶新-已处理\莫霖渊-特推款不干胶\96x64不干胶',
    '莫霖渊小不干胶': r'C:\Users\Administrator\Nutstore\1\义乌市植美工艺品\不干胶新-已处理\莫霖渊-特推款不干胶\莫霖渊小不干胶'
}

# 定义一个函数来搜索文件


def search_file(item_number, search_path):
    item_number_lower = item_number.lower()
    for root, _, files in os.walk(search_path):
        for file in files:
            if item_number_lower in file.lower():
                return True
    return False


# 读取Excel文件
excel_file = 'find.xlsx'
df = pd.read_excel(excel_file)

# 添加一列用于标注未找到的文件夹
df['未找到的内容如下'] = ""

# 遍历DataFrame中的每一行数据
for index, row in df.iterrows():
    group = row['组名']
    item_number = row['货号']
    quantity = row['数量']
    if pd.isna(group) or not group.strip():
        continue

    # 检查并搜索文件
    not_found_folders = []
    for folder_name, search_path in search_paths.items():
        if not search_file(item_number, search_path):
            not_found_folders.append(folder_name)

    # 如果在任一路径中未找到文件，将文件夹名称添加到未找到的文件夹列
    if not_found_folders:
        df.at[index, '未找到的内容如下'] = "未找到: " + ", ".join(not_found_folders)

# 保存修改后的DataFrame到新的Excel文件
df.to_excel('findx.xlsx', index=False)
