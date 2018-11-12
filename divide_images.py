import os
from shutil import copyfile

def create_n_dirs(path, n):
    for i in range(n):
        print(number_to_string(i+1))
        os.mkdir(path+"/"+number_to_string(i+1))


def number_to_string(number):
    if number < 10:
        return "00"+str(number)
    elif number < 100:
        return "0"+str(number)
    return number


def split_images(images_path, split_images_path):

    for name in os.listdir(images_path):
        print(name)
        class_number = name[0:3]
        copyfile(images_path+"/"+name, split_images_path+"/"+class_number+"/"+name)

def split_young_old(split_images_path):
    for folder in os.listdir(split_images_path):
        folder_path = split_images_path+"/"+folder
        print(folder_path)
        images_number = len(os.listdir(folder_path))
        print(images_number)
        #input()
        os_list = os.listdir(folder_path)
        os_list.sort()
        count = 1
        os.mkdir(folder_path+"/"+"young")
        os.mkdir(folder_path+"/"+"old")
        for image_name in os_list:
            print(image_name)
            if count <= int(images_number/2)+1:
                copyfile(folder_path + "/" + image_name, folder_path + "/" + "young" + "/" + image_name)
                print("young")
            else:
                copyfile(folder_path + "/" + image_name, folder_path + "/" + "old" + "/" + image_name)
                print("old")

            count = count + 1

            #input()


if __name__ == "__main__":

    images_path = "images"
    #create_n_dirs("divided_2", 82)

    #for name in os.listdir(images_path):
    #    print (name)
    #    print(name[:3])
    #    input()
    #split_images(images_path, "divided_2")
    split_young_old("divided_2")