import sys
import re
import datetime


def find_continuous_matches(file_path, query):
    with open(file_path, "r") as file:
        lines = file.readlines()

    # 初始化变量
    matches_count = 0
    buffer = []

    for line in lines:
        match = re.search(r"(\d+\.\d+),([a-zA-Z])$", line)
        if match:
            char = match.group(2)
            lb = len(buffer)
            if lb == 0 and char == query[0]:
                buffer.append(query[0])
            elif lb != 0:
                if lb < len(query) and query[lb] == char:
                    buffer.append(char)
                else:
                    buffer.clear()

            if "".join(buffer) == query:
                timestamp = float(match.group(1))
                date = datetime.datetime.fromtimestamp(timestamp).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                print(f'{date}: {"".join(buffer)}')
                matches_count += 1
                buffer.clear()

    # 输出总共的匹配次数
    print(f"Total Matches: {matches_count}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <query>")
        sys.exit(1)

    query = sys.argv[1]
    file_path = "key.log"  # 请替换为实际的文件路径

    find_continuous_matches(file_path, query)
