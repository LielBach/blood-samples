from blood_samples_reader import read_samples
from keras.layers import Input, Dense
from keras.models import Model
from keras.optimizers import SGD
from keras.losses import mean_squared_error
from keras.activations import relu
from sklearn.preprocessing import StandardScaler

blood_samples, ages = read_samples()
scaled_blood_samples = StandardScaler().fit_transform(blood_samples)

inputs = Input(shape=(scaled_blood_samples.shape[1],))

layer_1 = Dense(8012, activation=relu)(inputs)
layer_2 = Dense(2048, activation=relu)(layer_1)
layer_3 = Dense(512, activation=relu)(layer_2)

predictions = Dense(1)(layer_3)

model = Model(inputs=inputs, outputs=predictions)
model.compile(optimizer=SGD(lr=0.00001),
              loss=mean_squared_error)
model.fit(scaled_blood_samples, ages, validation_split=0.2, epochs=10000,
    verbose=2, batch_size=512)