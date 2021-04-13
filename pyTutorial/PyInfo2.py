def operator1():
    # = - * / ** // %
    print("算数运算符")
    # == != > < >= <=
    print("关系运算符")
    # = += -= *= /= %= //= **=
    # := 海象运算符，可在表达式内部为变量赋值
    print("赋值运算符")
    a = 'String'
    if(n := len(a) > 5):
        print(f"List is too long ({n} elements, expected <= 5)")
    # and or not
    print("逻辑运算符")
    c, d = 10, 20
    print("为什么c and d 会输出10" + c and d)
    if (c and d):
        print("1 - 变量 a 和 b 都为 true")
    else:
        print("1 - 变量 a 和 b 有一个不为 true")
    # & | ! << >> ~
    print("位运算符")
    # in, not in
    print("成员运算符")
    # is, is not
    # 判断两个对象是否是引用同一个
    print("身份运算符")
    # **	指数 (最高优先级)
    # ~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
    # * / % //	乘，除，求余数和取整除
    # + -	加法减法
    # >> <<	右移，左移运算符
    # &	位 'AND'
    # ^ |	位运算符
    # <= < > >=	比较运算符
    # == !=	等于运算符
    # = %= /= //= -= += *= **=	赋值运算符
    # is is not	身份运算符
    # in not in	成员运算符
    # not and or	逻辑运算符
    print("运算符优先级")

if __name__ == '__main__':
    operator1();