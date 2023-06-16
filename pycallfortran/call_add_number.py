'''
Author: wrry 
email: wangrry@hotmail.com
Date: 2023-06-16 01:01:32
LastEditors: wangrenruoyu@piesat.cn wangrry@hotmail.com
LastEditTime: 2023-06-16 10:17:19
FilePath: /nonsense/pycallfortran/call_add_number.py
Description: 
'''
import ctypes

# 加载.so文件
lib = ctypes.CDLL('./lib_add_number.so')

# 定义函数原型
add_number = lib.add_number_
add_number.restype = None
add_number.argtypes = [
    ctypes.c_float,  # number 1
    ctypes.c_float,  # number 2
    ctypes.POINTER(ctypes.c_float),  # result
]

# 创建输入变量
number1 = ctypes.c_float(1.2)
number2 = ctypes.c_float(2.3)

# 创建输出变量
result = ctypes.c_float()

# 调用函数
add_number(number1, number2, ctypes.byref(result))

# 输出结果
print("Result:", result.value)
exit()
import ctypes

# 加载.so文件
lib = ctypes.CDLL('./lib_add_number.so')

# 定义函数原型
add_number = lib.add_number_
add_number.restype = None
add_number.argtypes = [
    ctypes.c_float,# number 1
    ctypes.c_float,# number 2
    ctypes.POINTER(ctypes.c_float),# result
]

# 创建输入数组
number1 = ctypes.c_float(1.2)
number2 = ctypes.c_float(2.3)

# 创建输出数组
result = ctypes.c_float()

# 调用函数
add_number(number1, number2, ctypes.byref(result))

# 输出结果
print("Result:", result.value)


