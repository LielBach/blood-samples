from blood_samples_reader import read_samples
from keras.layers import Input, Dense
from keras.models import Model
from keras.optimizers import SGD
from keras.losses import mean_squared_error
from keras.activations import relu

blood_samples, ages = read_samples()

inputs = Input(shape=(20,))

layer_1 = Dense(512, activation=relu)(inputs)
layer_2 = Dense(4096, activation=relu)(layer_1)
layer_3 = Dense(4096, activation=relu)(layer_2)
layer_4 = Dense(4096, activation=relu)(layer_3)
layer_5 = Dense(128, activation=relu)(layer_4)

predictions = Dense(1)(layer_5)

model = Model(inputs=inputs, outputs=predictions)
model.compile(optimizer=SGD(lr=0.000001),
              loss=mean_squared_error)
model.fit(blood_samples, ages, validation_split=0.2, epochs=600, verbose=2, batch_size=6000)