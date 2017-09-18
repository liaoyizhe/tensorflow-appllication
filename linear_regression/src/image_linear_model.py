import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def train():
    # create real data
    x_data = np.random.rand(200).astype(np.float32)
    z_data = np.random.randint(100,103,size=(200)).astype(np.float32)
    y_data = x_data*0.1 + z_data
    # plot the real data
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(x_data, y_data)
    plt.ion()
    plt.show()
    #create td model
    Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    biases = tf.Variable(tf.zeros([1]))
    y = Weights*x_data + biases

    loss = tf.reduce_mean(tf.square(y-y_data))
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(loss)

    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)          # Very important

    for step in range(201):
        sess.run(train)
        if step % 20 == 0:
            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            prediction_value = x_data*sess.run(Weights) + sess.run(biases)
            # plot the prediction
            lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
            plt.pause(1)
    return
