from keras.engine import  Model
from keras.layers import Input
from keras_vggface import VGGFace
import numpy as np
from keras.preprocessing import image

def get_features(image_path):

    # FC7 Features
    vgg_model = VGGFace()  # pooling: None, avg or max
    out = vgg_model.get_layer('fc7').output
    vgg_model_fc7 = Model(vgg_model.input, out)

    # Change the image path with yours.
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    vgg_model_fc7_preds = vgg_model_fc7.predict(x)
    print(vgg_model_fc7_preds[0].shape)
    return vgg_model_fc7_preds[0]

if __name__ == "__main__":

    get_features("matt.jpg")
