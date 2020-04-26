# author: Ziming Guo
# time: 2020/3/4
"""
    游戏逻辑控制器，负责处理游戏核心算法．
    (Game logic controller, which handles the game's core algorithms)
"""

from model import DirectionModel
from model import Location
import random


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
            零元素移动到末尾.
            (Move the zero elements to the end)
        """
        for i in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            合并
            (merge)
        """
        self.__zero_to_end()

        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __move_left(self):
        """
            向左移动
            (move left)
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        """
            向右移动
            (move right)
        """
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def __move_up(self):
        """
            向上移动
            (move up)
        """
        self.__square_matrix_transpose()
        self.__move_left()
        self.__square_matrix_transpose()

    def __move_down(self):
        """
            向下移动
            (move down)
        """
        self.__square_matrix_transpose()
        self.__move_right()
        self.__square_matrix_transpose()

    def __square_matrix_transpose(self):
        """
            方阵转置(Square matrix transpose)
        :param sqr_matrix: 二维列表类型的方阵(Square matrix of two dimensional list)
        """
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]

    def move(self, dir):
        """
            移动
        :param dir: 方向,DirectionModel类型(direction, DirectionModel type)
        """
        if dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()

    def generate_new_number(self):
        """
            生成新数字
            (generate new numbers)
        """
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r_index][loc.c_index] = self.__select_random_number()
        # 因为在该位置生成了新数字，所以该位置就不是空位置了．
        self.__list_empty_location.remove(loc)

    def __select_random_number(self):
        return 4 if random.randint(1, 10) == 1 else 2

    def __get_empty_location(self):
        # 每次统计空位置，都先清空之前的数据，避免影响本次数据．
        # (Each time when counting the empty position, the previous data need to be cleared first to avoid affecting the data)
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append(Location(r, c))

    def is_game_over(self):
        """
            判断游戏是否结束(Determine if the game is over)
        :return: False表示没有结束 True 表示结束(False means the game is not ended, True means game is ended)
        """
        # 是否具有空位置(if there is any empty spaces)
        if len(self.__list_empty_location) > 0:
            return False

        for r in range(len(self.__map)):  # 0
            for c in range(len(self.__map[r]) - 1):  # 0 1 2
                if self.__map[r][c] == self.__map[r][c + 1] or self.__map[c][r] == self.__map[c + 1][r]:
                    return False

        return True


# ---------测试代码(test code)---------------


if __name__ == "__main__":
    controller = GameCoreController()
    # controller.move_left()
    # print(controller.map)
    # controller.move_down()
    # print(controller.map)

    # controller.move(DirectionModel.LEFT)
    # print(controller.map)
    # controller.move(DirectionModel.RIGHT)
    # print(controller.map)

    controller.generate_new_number()
    controller.generate_new_number()
    controller.generate_new_number()
    controller.generate_new_number()

    controller.is_game_over()
    print(controller.map)
