def change_word(filepath1, filepath2):
    with open(filepath1, 'r', encoding='utf-8') as file1, \
            open(filepath2, 'w', encoding='utf-8') as file2:
        for item in file1:
            if 'love' in item:
                item = item.replace('love', 'thank')
            file2.write(item)

if __name__ == '__main__':
    change_word('test.txt', 'output.txt')
