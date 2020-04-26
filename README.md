这个文件是要用来解释系统架构的(This file is used to explain the system architecture)

步骤(steps)：
    1. bll_edited.py 中的 GameCoreController 类是游戏算法的核心部分
       (GameCoreController class in bll_edited.py is the core algorithm of the game )
       变量(variable)：
           合并数字时使用的一维列表
           (one-dimensional list used to merge Numbers)
           移动数字时使用的二维列表
           (two-dimensional list used to merge Numbers)
       方法(method)：
          将零元素移至末尾(move zero to end)
          合并(merge)
          上移动(move up)
          下移动(move down)
          .....
    2. 在GameCoreController类中，定义产生随机数的方法.
       (In the GameCoreController class, define methods to generate random Numbers)
       需求:在空白的位置上
       (random numbers need to be generated in a blank space)
           随机数可能是2(90%),也可能是4(10%).
           (There's a 90 percent chance that the random number is 2, and a 10 percent chance that the random number is 4)

    3. 在GameCoreController类中，定义判断游戏是否结束的方法.
       (In the GameCoreController class, define method to determine if the game is over)
        1）是否具有空位置
           (If there is any blank spaces)
        2）横向竖向没有相同的元素
           (There is no any same elements in a row or a column) 
