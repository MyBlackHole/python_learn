import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.keras import layers, optimizers, datasets, Sequential
from resnet import resnet18

tf.random.set_seed(2345)


def preprocess(x, y):
    # [-1~1]
    x = tf.cast(x, dtype=tf.float32) / 255. - 0.5
    y = tf.cast(y, dtype=tf.int32)
    return x, y


(x, y), (x_test, y_test) = datasets.cifar100.load_data()
y = tf.squeeze(y, axis=1)
y = tf.one_hot(y, depth=100)
y_test = tf.squeeze(y_test, axis=1)
print(x.shape, y.shape, x_test.shape, y_test.shape)

train_db = tf.data.Dataset.from_tensor_slices((x, y))
train_db = train_db.shuffle(1000).map(preprocess).batch(128)

test_db = tf.data.Dataset.from_tensor_slices((x_test, y_test))
test_db = test_db.map(preprocess).batch(128)

sample = next(iter(train_db))
print('sample:', sample[0].shape, sample[1].shape,
      tf.reduce_min(sample[0]), tf.reduce_max(sample[0]))


def main():
    # [b, 32, 32, 3] => [b, 1, 1, 512]
    model = resnet18()
    model.build(input_shape=(None, 32, 32, 3))
    model.summary()
    model.compile(optimizer=optimizers.Adam(lr=0.01),
                  loss=tf.losses.CategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    checkpoint_path = "training/cp-{epoch:04d}.ckpt"
    # checkpoint_dir = os.path.dirname(checkpoint_path)
    # # model.save_weights(checkpoint_path.format(epoch=0))
    # # if os.path.isdir('training'):
    # #     latest = tf.train.latest_checkpoint(checkpoint_dir)
    # #     model.load_weights(latest)
    # #     loss, acc = model.evaluate(test_db, verbose=2)
    # #     print('loss:', loss, 'acc:', acc)
    cp_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_path,
        verbose=1,
        save_weights_only=True,
        save_freq=1)
    model.fit(train_db, epochs=500, validation_data=test_db, validation_steps=2, callbacks=[cp_callback], verbose=0)
    # model.fit(train_db, epochs=500, validation_data=test_db, validation_steps=2)


if __name__ == '__main__':
    main()
