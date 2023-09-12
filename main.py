import requests
from bs4 import BeautifulSoup

# 目标网页的URL
url = "https://www.luogu.com.cn/problem/list"

# 发起GET请求
response = requests.get(url)

# 解析HTML内容
soup = BeautifulSoup(response.text, "html.parser")

# 找到包含题目的HTML元素
problem_elements = soup.find_all("div", class_="lg-list-item")

# 遍历每个题目元素
for problem_element in problem_elements:
    # 提取题目难度
    difficulty = problem_element.find("span", class_="lg-right-difficulty").text.strip()

    # 提取算法
    algorithm = problem_element.find("span", class_="lg-right-algorithm").text.strip()

    # 提取来源
    source = problem_element.find("span", class_="lg-right-source").text.strip()

    # 提取标题
    title = problem_element.find("a", class_="lg-right-title").text.strip()

    # 提取题目编号
    problem_id = problem_element.find("span", class_="lg-right-id").text.strip()

    # 打印题目信息
    print("题目难度:", difficulty)
    print("算法:", algorithm)
    print("来源:", source)
    print("标题:", title)
    print("题目编号:", problem_id)
    print("--------------------")
