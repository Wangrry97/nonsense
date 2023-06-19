'''
Author: wrry 
email: wangrry@hotmail.com
Date: 2023-06-16 01:01:32
LastEditors: wangrenruoyu@piesat.cn wangrry@hotmail.com
LastEditTime: 2023-06-19 13:49:32
FilePath: /nonsense/pycallfortran/call_libirbem.py
Description: 
'''
import ctypes
import numpy as np

# 加载库文件
libirbem = ctypes.CDLL('libirbem.so')

# 设置函数参数类型
libirbem.get_ae8_ap8_flux_.argtypes = [
    ctypes.POINTER(ctypes.c_int),  # ntmax
    ctypes.POINTER(ctypes.c_int),  # whichm
    ctypes.POINTER(ctypes.c_int),  # whatf
    ctypes.POINTER(ctypes.c_int),  # nene
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),  # energy
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),  # BBo
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),  # L
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS')   # flux
]

# 设置函数返回类型
libirbem.get_ae8_ap8_flux_.restype = None

# 创建参数变量
ntmax = 100000
whichm = 3
whatf = 3
nene = 1

energy = np.zeros(100000, dtype=np.float64)
BBo = np.zeros(100000, dtype=np.float64)
L = np.zeros(100000, dtype=np.float64)
flux = np.zeros(2500000, dtype=np.float64)

# 调用函数
libirbem.get_ae8_ap8_flux_(
    ctypes.pointer(ctypes.c_int(ntmax)),
    ctypes.pointer(ctypes.c_int(whichm)),
    ctypes.pointer(ctypes.c_int(whatf)),
    ctypes.pointer(ctypes.c_int(nene)),
    energy,
    BBo,
    L,
    flux
)

# 打印结果
print("Flux:", flux)
