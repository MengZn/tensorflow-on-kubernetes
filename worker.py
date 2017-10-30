import tensorflow as tf

with tf.device("/job:worker/task:0"):
    a = tf.constant([1.5, 6.0], name='a')
    b = tf.Variable([1.5, 3.2], name='b')
    c = (a * b) + (a / b)
    d = c * a
    y = tf.assign(b, d)

with tf.Session("grpc://tf-worker.default.svc.cluster.local:2222") as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('/notebooks/logs/', graph=tf.get_default_graph())
    print(sess.run(y))
