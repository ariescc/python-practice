import re


def count_word(filepath):
    with open(filepath) as file:
        data = file.read()
        words = re.findall(r'[a-zA-Z]+', data)
        count = len(words)
        print(count)
    return count

if __name__ == '__main__':
    print(count_word('test.txt'))
