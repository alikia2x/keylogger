import re
from collections import Counter

# 读取文件
file_path = "key.log"
with open(file_path, "r") as file:
    content = file.readlines()

# 使用正则表达式匹配行尾的"UNIX时间戳,字母"
matches = [re.search(r"(\d+\.\d+),([\S])$", line) for line in content]

# 获取匹配的字母并转换为小写
matches = [match.group(2).lower() if match else None for match in matches]

# 过滤掉没有匹配到的行
matches = [match for match in matches if match is not None]

# 计算字母的频率
counter = Counter(matches)

# 按频率降序排序
sorted_results = sorted(counter.items(), key=lambda x: x[1], reverse=True)

# 输出结果
for letter, count in sorted_results:
    print(f"{letter}: {count}")
