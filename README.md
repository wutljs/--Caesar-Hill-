# --Caesar-Hill-
通过python程序来对两个古典加密算法的模拟实现

对于**Caesar**加密算法来说，本身是非常简单的，使用双方需要事先规定好一个密钥（字符串），设置偏移量*k*，即可完成加密和解密的操作；

而**Hill**加密算法则要比**Caesar**算法要复杂一些，**Hill**算法运用了矩阵论中的**线性变换原理**，以此来隐蔽单字母频率特性。但是在笔者测试中发现

如果密钥矩阵*K*比较复杂的话，在解密时会产生一定的误差，即求*K*的逆矩阵时，该逆矩阵中的元素并非都是整数，这就导致在对*26*取模运算得到的数值会出现问题

因此，笔者猜测*K*矩阵应该是要符合一些条件的。很遗憾，笔者的**线性代数**也仅仅是学到了一些皮毛，故无法通过数学上的求证来找到*K*矩阵应该符合的特点。
