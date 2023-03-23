'''测试Hill加密算法'''

from ClassicCrypto import *
import numpy as np

p_str = 'are'

# 来自于 https://www.cnblogs.com/labster/p/13848395.html 的案例
# h = Hill()
# key = np.matrix([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
# c_str = h.e(p_str, key)
# print(c_str)

h = Hill()
key = np.matrix([[1, 2, 3], [1, 1, 2], [0, 1, 2]])
c_str = h.e(p_str, key)
p_c_str = h.d(c_str, key)
print('明文是{},加密后的密文是{},密文被解密后是{}.'.format(p_str, c_str, p_c_str))
