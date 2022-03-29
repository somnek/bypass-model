import tensorflowjs as tfjs
from tensorflow import keras

model = keras.models.load_model('/home/mlp/project/ocr/bypass-model/efficient_e20_b32.h5')
tfjs.converters.save_keras_model(model, './')
print('Conversion completed.')
