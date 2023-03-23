import string
import numpy as np
import random


class Caesar:
    '''
    Caesar密码:
    * 加密算法:c = E(k,m) = (m + k) mod 26
    * 解密算法:m = D(k,c) = (c - k) mod 26
    '''

    dig_str = string.ascii_lowercase

    def e(self, p_str, k):
        '''加密算法'''
        c_str = ''
        for item in p_str:
            dig_index = (self.dig_str.index(item) + k) % 26
            c_str += self.dig_str[dig_index]

        return c_str

    def d(self, c_str, k):
        '''解密算法'''
        p_str = ''
        for item in c_str:
            dig_index = (self.dig_str.index(item) - k) % 26
            p_str += self.dig_str[dig_index]

        return p_str


class Hill:
    '''
    Hill密码:
    * 加密算法:C = E(K,P) = KP mod 26
    * 解密算法:P = D(K,P) = K^(-1)C mod 26
    注:以上C,P和K均为矩阵
    '''

    dig_str = string.ascii_lowercase

    def __warning(self):
        print("您的密钥不符合Hill密码相关的要求,您可以选择调用get_random_key方法来生成一个随机密钥.")

    def __check_key(self, key, **kwargs):
        '''检查密钥矩阵是否符合要求'''
        matrix_key = np.matrix(key)

        # 检测用户输入矩阵的行、列是否符合要求
        # 这段代码不会被get_random_key方法调用
        if kwargs != {}:
            p_str_length = kwargs['p_str_length']
            x, y = matrix_key.shape
            if x != p_str_length or y != p_str_length:
                self.__warning()
                return False

        # 检查矩阵是否可逆
        try:
            useless_temp = matrix_key.I
            return True
        except np.linalg.LinAlgError:
            self.__warning()
            return False

    def get_random_key(self, p_str):
        '''生成随机密钥'''
        p_str_length = len(p_str)
        arr_key = np.empty([p_str_length, p_str_length], dtype=int)

        # 生成随机数密钥
        for i in range(p_str_length):
            for j in range(p_str_length):
                arr_key[i][j] = random.randint(0, 25)
        matrix_key = np.matrix(arr_key)

        # 检查密钥是否为可逆矩阵
        if self.__check_key(matrix_key):
            return matrix_key
        else:
            self.get_random_key(p_str)

    def e(self, p_str, key):
        '''加密算法'''
        matrix_key = np.matrix(key)
        p_str_length = len(p_str)
        if self.__check_key(matrix_key, p_str_length=p_str_length):
            # 将明文字符串转化为矩阵
            arr_p_str = [self.dig_str.index(i) for i in p_str]
            matrix_p_str = np.matrix(arr_p_str)

            # Hill加密得出密文初始矩阵
            matrix_c_str = np.dot(matrix_key, matrix_p_str.T)
            # 将初始矩阵中的元素 mod 26,生成密文
            arr_c_str = [i[0] % 26 for i in np.array(matrix_c_str)]
            c_str = ''
            for i in arr_c_str:
                c_str += self.dig_str[i]

        else:
            return None

        return c_str

    def d(self, c_str, key):
        '''解密算法(逆矩阵中元素不是整数的问题没有解决)'''
        matrix_key = np.matrix(key)
        if self.__check_key(matrix_key, p_str_length=len(c_str)):
            # 将密文字符串转化为矩阵
            arr_c_str = [self.dig_str.index(i) for i in c_str]
            matrix_c_str = np.matrix(arr_c_str)

            # Hill加密得出密文初始矩阵
            matrix_p_str = np.dot(matrix_key.I, matrix_c_str.T)
            # 将初始矩阵中的元素 mod 26,生成密文
            arr_p_str = [int(i[0]) % 26 for i in np.array(matrix_p_str)]
            p_str = ''
            for i in arr_p_str:
                p_str += self.dig_str[i]
        else:
            return None

        return p_str
