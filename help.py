from os import walk


def import_folder(path):
    surface_list =  []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path+image
            print(full_path)

    return surface_list
