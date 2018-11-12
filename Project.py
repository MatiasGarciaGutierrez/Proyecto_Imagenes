import os
from keras.engine import  Model
from keras.layers import Input
from keras_vggface import VGGFace
import numpy as np
from keras.preprocessing import image
from scipy.io import savemat


# FC7 Features
vgg_model = VGGFace()  # pooling: None, avg or max
out = vgg_model.get_layer('fc7').output
vgg_model_fc7 = Model(vgg_model.input, out)


def get_features(image_path):

    # Change the image path with yours.
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    vgg_model_fc7_preds = vgg_model_fc7.predict(x)
    #print(vgg_model_fc7_preds[0].shape)
    return vgg_model_fc7_preds[0]


def create_all_features(path):
    young_descriptors = []
    old_descriptors = []
    for folder in os.listdir(path):
        folder_path = path+"/"+folder
        young_descriptors = create_features(folder_path, "young", young_descriptors)
        old_descriptors = create_features(folder_path, "old", old_descriptors)
    return young_descriptors, old_descriptors


def create_features(path, age_group, list):
    for image in os.listdir(path+"/"+age_group):
        label = float(image[0:3])
        age = float(image[4:6])
        image_path = path+"/"+age_group+"/"+image
        features = get_features(image_path)
        list.append([features, label, age, age_group])
        #print(image_path)
    return list


def save_features(old_features, young_features):
    savemat('datosImagenes.mat', {'old': old_features, 'young': young_features})
    return


if __name__ == "__main__":
    young_descriptors, old_descriptors = create_all_features("divided_2")
    save_features(old_descriptors, young_descriptors)