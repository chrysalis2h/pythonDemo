def symbol1():
    print("标识符");
    # 可以是字母、数字、下划线。
    # 以下划线开头的变量（_foo），不能直接访问，需要通过类提供的接口来访问。
    # 以双下换线开头的变量（__foo）， 代表私有变量。
    # 类似__foo__，代表python中的特殊的方法专用的标识
    # python中的保留关键字，都是小写的。
    print("行和缩进");
    # python是用缩进来写模块，缩进数量是可变的，但是必须相同
    # python对格式要求严格
    print("多行语句")
    # python可以类似shell中，以（\）讲一句分为多行展示
    print("引号")
    # 引号可以用（'', "", """"""）
    # """"""可以多行展示
    print("空行")
    # 用空行来标识一段新代码的开始。空行也是程序代码的一部分
    print("等待用户输入")
    print("同一行显示多条语句")
    print("换行")

def baseDataType():
    # 基本数字类型
    # 整数
    intValue = 1
    # 布尔 True False
    booleanValue = False
    # 浮点数
    floatValue = 1.0
    # 复数
    complexValue = 1 + 2j
    print("基本数据类型")
    '''
    字符串
    转义符（\）。使用r可以来防止转义
    字符串可以用+连接。用*来重复（str*2)。
    两种索引方式，从左往右以0开始，从右往左以-1开始
    字符串不可变
    没有单独的字符类型，一个字符就是长度为 1 的字符串
    字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
    '''
    title1 = "String   ---   "
    str = "python demo"
    # 输出字符串
    print(title1 + str)
    # 输出第一个到倒数第二个的所有字符
    print(title1 + str[0:-1])
    # 输出字符串第一个字符
    print(title1 + str[0])
    # 输出从第三个开始到第五个的字符
    print(title1 + str[2:5])
    # 输出从第三个开始后的所有字符
    print(title1 + str[2:])
    # 输出从第二个开始到第五个且每隔两个的字符
    print(title1 + str[1:5:2])
    # 输出字符串两次
    print(title1 + str * 2)
    # 连接字符串
    print(title1 + str + "print")

def baseDataType2():
    # 变量不需要声明，使用前必须赋值，赋值后才真正被创建
    floatVal = 100.0
    print("变量")
    # 多个变量复制
    a, b, c = 1, "2", 3.0
    print("多个变量")
    # 基本数据类型
    # Number - 不可变
    a, b, c, d = 666, True, 6.6, 1+2j
    print(type(a), type(b), type(c), type(d))
    # String - 不可变
    print("")
    # Tuple - 不可变
    print("")
    # List - 可变
    print("")
    # Set - 可变
    print("")
    # Dictionary - 可变
    print("")
    print("")
    print("")
    print("")
    print("")
if __name__ == '__main__':
    baseDataType();