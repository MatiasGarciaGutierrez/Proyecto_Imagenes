import numpy as np
from keras_vggface.vggface import VGGFace
from keras.preprocessing import image
from keras_vggface import utils
from sklearn.neighbors import NearestNeighbors


if __name__ == "__main__":
    model = VGGFace(model='vgg16', include_top= False) # or VGGFace() as default
    img = image.load_img('matt.jpg', target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = utils.preprocess_input(x, version=1)  # or version=2
    preds = model.predict(x)
    print(preds)
    print(preds.shape)
