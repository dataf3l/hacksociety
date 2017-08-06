import tensorflow as tf

a = tf.placeholder(tf.float32)
x = tf.constant([90210.0])
b = tf.add(a, x)
tf.global_variables_initializer()
dictionary={a: [ [ [1,2,3],[4,5,6],[7,8,9],[10,11,12] ] , [ [13,14,15],[16,17,18],[19,20,21],[22,23,24] ] ] }

with tf.Session() as session:
    print(session.run([b], dictionary))
    #print(session.run([b], {a: [90.0]}))



a = tf.constant([5])
b = tf.constant([2])
c = tf.add(a,b)
d = tf.subtract(a,b)

with tf.Session() as session:
    result = session.run(c)
    print('c =: %s' % result)
    result = session.run(d)
    print('d =: %s' % result)

# dict, keys are tensors
# https://github.com/rstudio/tensorflow/issues/6
# https://github.com/tensorflow/tensorflow/issues/3378
