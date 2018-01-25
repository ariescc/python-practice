import os

# 遍历指定目录，显示目录下所有的文件名
def get_each_file(file_path):
    path_dir = os.listdir(file_path)
    for all_dir in path_dir:
        child = os.path.join('%s%s' % (file_path, all_dir))
        print(child)


# 读取文件内容打印
def read_file(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        print(f.read())


# 输入文字，写入指定文件并保存到指定文件夹
def write_file(filename):
    with open(filename, 'a', encoding = 'utf-8') as f:
        f.write('categories: 技术篇')


if __name__ == '__main__':
    #get_each_file('Q:\github\source\_posts')

    filename = 'Q:\\ariescc\哈哈.md'

    lines = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            lines.append(line)
        f.close()

    print(lines)
    
    lines.insert(4, 'categories: 技术篇\n')
    s = ''.join(lines)
    with open(filename, 'w+', encoding = 'utf-8') as f:
        f.write(s)
        f.close()

    del lines[:]
    print(lines)


#Q:\github\source\_posts\VBA学习笔记（二）.md
