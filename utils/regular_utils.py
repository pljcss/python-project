import re

def re_demo():
    str1 = """
        <span class="mid-rank-stars mid-str50" title=""></span>
    """

    str1 = """
    <span class="mid-rank-stars mid-str50" title=""></span>
    """


    print(str1.strip())
    print("-"*20)

    # 获取数字
    print(re.findall(r"\d+\.?\d*",str1.strip())[0])



if __name__ == '__main__':
    re_demo()