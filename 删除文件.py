import os

# 读取txt文件中的货号列表


def read_product_codes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

# 遍历目录和子目录，查找并删除文件


def find_and_delete_files(directory, product_codes):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件名是否与货号完全匹配
            if file in product_codes:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"已删除: {file_path}")
                product_codes.remove(file)  # 从列表中移除已删除的货号
            else:
                # 如果货号列表为空，说明所有货号都已找到并删除
                if not product_codes:
                    return
    # 如果函数没有提前返回，说明有货号未找到
    for code in product_codes:
        print(f"找不到: {code}")

# 主函数


def main():
    directory = input("请输入要遍历的目录路径: ")
    txt_file = './name.txt'
    product_codes = read_product_codes(txt_file)
    find_and_delete_files(directory, product_codes)


if __name__ == "__main__":
    main()
