import tensorflow as tf


def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model


def main(y_train=None, x_train=None):
    model = create_model()
    train_data = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(32)
    model.fit(train_data, epochs=5)
    model.save('gs://bucket/model')


if __name__ == '__main__':
    main()
