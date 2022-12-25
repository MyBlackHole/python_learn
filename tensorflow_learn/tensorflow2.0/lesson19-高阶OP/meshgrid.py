import tensorflow as tf

import matplotlib.pyplot as plt


def func(x):
    """

    :param x: [b, 2]
    :return:
    """
    z = tf.math.sin(x[..., 0]) + tf.math.sin(x[..., 1])

    return z


x = tf.linspace(0., 2 * 3.14, 500)
y = tf.linspace(0., 2 * 3.14, 500)
# [50, 50]
point_x, point_y = tf.meshgrid(x, y)
# [50, 50, 2]
points = tf.stack([point_x, point_y], axis=2)
# points = tf.reshape(points, [-1, 2])
print('points:', points.shape)
z = func(points)
print('z:', z)
print('z.shape:', z.shape)

# 创建图像实例
plt.figure('plot 2d func value')
# 绘制图像
plt.imshow(z, origin='lower', interpolation='none')
# 增加等高线分布渐变色条
plt.colorbar()

# 创建图像实例
plt.figure('plot 2d func contour')
# 等高线图
plt.contour(point_x, point_y, z)
# 增加等高线分布渐变色条
plt.colorbar()
plt.show()
