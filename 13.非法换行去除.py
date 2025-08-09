import re

illegal_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '\n']
def clean_filename(filename):
    for char in illegal_chars:
        filename = filename.replace(char, "")
    return filename

# 测试
filename = "test\nfile.txt"
print(clean_filename(filename))