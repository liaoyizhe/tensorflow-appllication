# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

# 基本数据 使用 NumPy 生成假数据(phony data), 总共 100 个点.
# 随机输入 生成2行100列的x_data
x_data = np.float32(np.random.rand(2, 100))
# 矩阵相乘 1行2列[0.100, 0.200]x2行100列随机数据 再加上 0.3
y_data = np.dot([0.100, 0.200], x_data) + 0.300

def train():
    # 构造一个线性模型
    # tf的模型变量 生成1行1列[0]矩阵 b其实是我们要预测的值
    b = tf.Variable(tf.zeros([1]))
    # tf的模型变量 生成1行2列最大值为1.0最小值为-1.0的随机矩阵 W其实就是我们要预测的值
    W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
    # tf变量矩阵相运算 W与x_data相乘再加上b 生成1行100列的矩阵
    y = tf.matmul(W, x_data) + b

    # 最小化方差
    # 求出误差值 将tf预测变量y减去实际值y_data(实际上是一维数组的内积),得出的结果(1行1列的数值),再求出平均值
    loss = tf.reduce_mean(tf.square(y - y_data))
    # 将tf的误差访问调整为0.5,一般都是在1以内
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(loss)

    # 初始化变量
    init = tf.global_variables_initializer()

    # 启动图 (graph)
    sess = tf.Session()
    # 将tf模型跑起来
    sess.run(init)

    # 拟合平面
    # tf将上述模型做了200次训练,每隔20次打印出一次预测结果W以及b
    for step in range(0, 201):
        sess.run(train)
        if step % 20 == 0:
            print (step, sess.run(W), sess.run(b))
    ## 总结,实质上就是拿到一份线性模型的打点数据x,y。然后用tf运行200次，估算出预测的值W以及b。事实上我并不觉得这个例子很好，毕竟是矩阵的线性模型,新人比较难理解。如果换成 y = ax + b 就好了
    ## 在实际开发中，我们的打点数据可能会分散，但也符合一定的线性回归，也可以按照这个预测出W以及b值
    return
