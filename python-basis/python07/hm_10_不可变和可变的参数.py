def demo(num, num_list):
    print("函数内部的代码")
    print("%d --- %d" % (num, id(num)))
    print("%s --- %d" % (num_list, id(num_list)))

    # 在函数内部，针对参数使用赋值语句，不会修改到外部的实参变量
    num = 100
    num_list = [1, 2, 3]

    print("%d --- %d" % (num, id(num)))
    print("%s --- %d" % (num_list, id(num_list)))
    print("函数执行完成")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print("%d --- %d" % (gl_num, id(gl_num)))
print("%s --- %d" % (gl_list, id(gl_list)))
