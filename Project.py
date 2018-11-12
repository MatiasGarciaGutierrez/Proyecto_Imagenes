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
    """

    :param image_path(str): Path of a image to extract features with VGG-face.
    :return: A 4096 feature vector.
    """
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    vgg_model_fc7_preds = vgg_model_fc7.predict(x)
    #print(vgg_model_fc7_preds[0].shape)
    return vgg_model_fc7_preds[0]


def create_all_features(path):
    """

    :param path: path of the divided dataset.
    :return: two list of all young and old photos descriptors.
    """
    young_descriptors = []
    old_descriptors = []
    for folder in os.listdir(path):
        folder_path = path+"/"+folder
        young_descriptors = create_features(folder_path, "young", young_descriptors)
        old_descriptors = create_features(folder_path, "old", old_descriptors)
    return young_descriptors, old_descriptors


def create_features(path, age_group, list):
    """

    :param path: path of a folder with images.
    :param age_group: young/old.
    :param list: list of descriptors.
    :return: the list receive with new features append.
    """
    for image in os.listdir(path+"/"+age_group):
        label = float(image[0:3])
        age = float(image[4:6])
        image_path = path+"/"+age_group+"/"+image
        features = get_features(image_path)
        list.append([features, label, age, age_group])
        #print(image_path)
    return list


def save_features(old_features, young_features):
    """

    :param old_features: features of old ages
    :param young_features: features of young ages
    :return: nothing.
    """
    savemat('datosImagenes.mat', {'old': old_features, 'young': young_features})
    return


if __name__ == "__main__":
    young_descriptors, old_descriptors = create_all_features("divided_2")
    save_features(old_descriptors, young_descriptors)