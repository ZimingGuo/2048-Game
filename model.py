# author: Ziming Guo
# time: 2020/3/4

class DirectionModel:
    """
        方向数据模型
        枚举  常量(命名全部大写)
    """
    # 在整数基础上，添加一个人容易识别的"标签"
    # (On the basis of integers, add a tag that one can easily recognize.)
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Location:
    """
        位置(position)
    """
    def __init__(self, i, m):
        self.i_index = i
        self.m_index = m
