'''
Author: wrry 
email: wangrry@hotmail.com
Date: 2023-06-16 01:01:32
LastEditors: wangrenruoyu@piesat.cn wangrry@hotmail.com
LastEditTime: 2023-06-16 13:47:06
FilePath: /nonsense/pycallfortran/call_libirbem.py
Description: 
'''
import ctypes
import numpy as np

# 加载共享库
lib = ctypes.CDLL('./libirbem.so')

# 定义函数原型
get_flux = lib.get_ae8_ap8_flux_
get_flux.restype = None
get_flux.argtypes = [
    ctypes.c_int,              # ntmax
    ctypes.c_int,              # whichm
    ctypes.c_int,              # whatf
    ctypes.c_int,              # nene
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),  # energy
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),  # BBo
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),  # L
    np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'),  # flux
]

# 创建输入数组
ntmax = 5   #ctypes.pointer(ctypes.c_int(5))  # 根据需求设置值
whichm = 3  #ctypes.pointer(ctypes.c_int(3))  # 根据需求设置值
whatf = 3   #ctypes.pointer(ctypes.c_int(3))  # 根据需求设置值
nene = 1    #ctypes.pointer(ctypes.c_int(1))
energy = np.zeros((2, 25), dtype=np.float64)  # 根据需求创建数组
BBo = np.zeros(5, dtype=np.float64)  # 根据需求创建数组
L = np.zeros(5, dtype=np.float64)  # 根据需求创建数组
flux = np.zeros((10000, 25), dtype=np.float64)  # 根据需求创建数组

# 按照示例程序给数组赋值
BBo[:] = 2.5
L[:] = 2.15
energy[0, 0] = 0.5
energy[1, 0] = 0.7

# 调用函数
get_flux(ntmax, whichm, whatf, nene, energy, BBo, L, flux)

# 打印结果
print("Flux:", flux)
