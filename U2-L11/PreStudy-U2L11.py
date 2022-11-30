# 1. 什么是模块？
# 模块是python程序架构的一个核心概念
# 模块名需要符合标识符的命名规则
# 在模块中定义的全局变量、函数、类都是提供给外界直接使用的工具
# 模块就像工具包，要想使用这个工具包中的工具，就要先导入这个模块

# 2. 如何导入模块？有哪些方式？
# 1 import 模块1, 模块2(不推荐)
# 2 import 模块1
#   import 模块2
# 3 import 模块1 as 简化后的名字1(可以用另一个名字来代替原本的模块)---单纯是个别名
#   import 模块2 as 简化后的名字2(简化后的名字要用大驼峰)

# 3. 不同的模块导入方式有什么区别？
# 从某一个模块中导入部分工具，就可以使用
# from 模块名1 import 工具名
# import模块名就是将模块中所有的工具导入，通过模块名/别名访问
# 不需要通过模块名，可以直接通过使用模块提供的工具--全局变量，模块，类
# 如果两个模块有同名函数，第二个会覆盖掉第一个的函数
# 解决方法from 模块名1 import 工具名 as 别名

# 4. 导入模块时，模块的搜索顺序是怎样的？
# 1搜索 当前目录 指定模块名的文件，如果有就直接导入
# 2如果没有再搜索 系统目录
# 3给模块命名是不要和系统的模块文件重名
# __file__可以查看模块的完整路径