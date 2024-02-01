from collections import defaultdict
import re

# 读取key.log文件
with open("key.log", "r") as file:
    content = file.read()

# 匹配组合键的正则表达式
pattern = r'(Key\.(?:alt|ctrl|cmd)\+[a-zA-z0-9.+]+)'

# 使用正则表达式进行匹配
matches = re.findall(pattern, content)

# 统计组合键出现的频率
frequency = defaultdict(int)
for match in matches:
    frequency[match] += 1

# 按照频率排序
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

# 打印结果
for key, count in sorted_frequency:
    print(f"{key}: {count}")
