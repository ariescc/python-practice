import os

# 遍历指定目录,获取所有文件名
def get_each_filename(folder_path):
    path_dir = os.listdir(folder_path)
    child_dirs = []
    for all_dir in path_dir:
        child = os.path.join('%s\%s' % (folder_path, all_dir))
        child_dirs.append(child)

    #print(child_dirs)
    return child_dirs

# 每个文件中追加内容
def insert_content(filename):
    
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
    

# 入口函数
def run(folder_path):
    
    # 获取所有子文件列表
    children = get_each_filename(folder_path)

    for childname in children:
        insert_content(childname)

    
if __name__ == '__main__':
    run('Q:\github\source\_posts')
    #get_each_filename('Q:\github\source\_posts')

