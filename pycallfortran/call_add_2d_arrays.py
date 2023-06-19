'''
Author: wangrenruoyu@piesat.cn 
email: wangrry@hotmail.com
Date: 2023-06-16 11:31:09
LastEditors: wangrenruoyu@piesat.cn wangrry@hotmail.com
LastEditTime: 2023-06-19 13:38:40
FilePath: /nonsense/pycallfortran/call_add_2d_arrays.py
Description: 
'''
import ctypes
import numpy as np

# 加载.so文件
lib = ctypes.CDLL('./libadd_2d_arrays.so')

# 定义函数原型
add_2d_arrays = lib.add_2d_arrays_
add_2d_arrays.restype = None
add_2d_arrays.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),  # array
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),  # result
    ctypes.c_int,                                                    # nrows
    ctypes.c_int                                                     # ncols
]

# 创建输入二维数组
array = np.array([[1.0, 2.0, 3.0, 4.0],
                  [4.0, 5.0, 6.0, 7.0]], dtype=np.float64)
nrows, ncols = array.shape
print(nrows, ncols)
# 创建输出一维数组
result = np.zeros(nrows, dtype=np.float64)

# nrows = ctypes.c_int(nrows)
# ncols = ctypes.c_int(ncols)



# 调用函数
add_2d_arrays(array, result, nrows, ncols)

# 输出结果
print("Result:", result)
