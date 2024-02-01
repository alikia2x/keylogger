from collections import defaultdict
import re
import datetime

# 读取文件
file_path = 'key.log'
with open(file_path, 'r') as file:
    lines = file.readlines()

# 匹配时间戳
pattern = re.compile(r'^(\d+\.\d+),')

# 使用字典记录每一天的行数
daily_counts = defaultdict(int)
current_date = None

# 遍历文件内容
for line in lines:
    match = pattern.match(line)
    if match:
        timestamp = float(match.group(1))
        date = datetime.datetime.fromtimestamp(timestamp).date()
        # 如果日期改变，则更新当前日期并将计数器重置为1
        if date != current_date:
            current_date = date
            daily_counts[current_date] = 1
        else:
            daily_counts[current_date] += 1

# 输出每一天的行数
for date, count in sorted(daily_counts.items()):
    print(f'{date}: {count}')

