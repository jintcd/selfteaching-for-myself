
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def is_leap(year):
    r = False
    if year % 4 == 0:
        r = True
        if year % 100 == 0:
            if year % 400 != 0:
                r = False
    return r

is_leap(4) is True
is_leap(200) is False
is_leap(220) is True
is_leap(400) is True

#会发现自己的错误，错误的解释在以下位置https://docs.python.org/3/library/exceptions.html
#错误分类，1、语法错误（Syntax Errors）2、意外（Exceptions）
# 主要学习的内容是 函数编辑思路 + 测试方法
# 闰年的计算方法例子设计思路,判断一件事的逻辑,也就是步骤;
# 闰年定义: 1.年份被4整除;2.年份能被100整除，不能被400整除不是闰年；3.排除1中的2不满足项目；