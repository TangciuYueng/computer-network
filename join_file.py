import os

def merge_files(folder_name, output_file_name):
    # 获取文件夹下所有小文件的路径
    file_paths = [os.path.join(folder_name, file) for file in os.listdir(folder_name) if os.path.isfile(os.path.join(folder_name, file))]

    # 按照文件名排序
    file_paths.sort()

    # 合并小文件为一个完整文件
    with open(os.path.join(folder_name, output_file_name), 'wb') as output_file:
        for file_path in file_paths:
            with open(file_path, 'rb') as input_file:
                output_file.write(input_file.read())

if __name__ == "__main__":
    # 输入文件夹名和输出文件名
    folder_name = input("请输入文件夹名: ")
    output_file_name = input("请输入输出文件名: ")

    # 调用函数进行文件合并
    merge_files(folder_name, output_file_name)

    print("文件合并完成。")
