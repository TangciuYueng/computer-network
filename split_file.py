import os

def split_file(input_file_path, chunk_size):
    # 创建目录名为文件名的文件夹
    folder_name = os.path.splitext(os.path.basename(input_file_path))[0]
    os.makedirs(folder_name, exist_ok=True)

    with open(input_file_path, 'rb') as f:
        index = 1
        while True:
            # 读取指定大小的数据
            data = f.read(chunk_size)
            if not data:
                break

            # 构造分块文件名
            chunk_file_name = os.path.join(folder_name, f'{index:03d}_{os.path.basename(input_file_path)}')
            
            # 写入分块文件
            with open(chunk_file_name, 'wb') as chunk_file:
                chunk_file.write(data)

            index += 1

if __name__ == "__main__":
    # 输入文件路径和分块大小
    file_path = input("请输入文件路径: ")
    chunk_size = int(input("请输入分块大小（字节数）: "))

    # 调用函数进行文件分块
    split_file(file_path, chunk_size)

    print("文件分割完成。")
