import os
import random

sub_paths = {
    'primaries': ['/train', '/valid', '/test'],
    'images': ['/train/images', '/valid/images', '/test/images',], 
    'labels': ['/train/labels', '/valid/labels', '/test/labels'],
            }

dir_path = "/home/mvanslyke/Documents/GitHub/SpringBoardDataScience/Capstone_Project_2/Data"
train_path = dir_path + sub_paths['primaries'][0]
train_imgs = sorted(os.listdir(dir_path + sub_paths['images'][0]))
train_targets = sorted(os.listdir(dir_path + sub_paths['labels'][0]))

val_path = dir_path + sub_paths['primaries'][1]
val_imgs = sorted(os.listdir(dir_path + sub_paths['images'][1]))
val_targets = sorted(os.listdir(dir_path + sub_paths['labels'][1]))

test_path = dir_path + sub_paths['primaries'][2]
test_imgs = sorted(os.listdir(dir_path + sub_paths['images'][2]))
test_targets = sorted(os.listdir(dir_path + sub_paths['labels'][2]))

def unconvert(width, height, x, y ,w, h):
    xmax = int((x * width) + (w * width) / 2.0)
    xmin = int((x * width) - (w * width) / 2.0)
    ymax = int((y * height) + (h * height) / 2.0)
    ymin = int((y * height) - (h * height) / 2.0)
    
    return xmin, ymin, xmax, ymax

idx_train = random.randint(0, len(train_imgs))

train_image_paths = os.path.join(train_path, 'images', train_imgs[idx_train])
train_target_paths = os.path.join(train_path, 'labels', train_targets[idx_train])

file = open(train_image_paths, 'r')


def import_boxes(list):
    '''
    Function for converting the text data in the labels files into functional
    dictionaries:  Given a list from a read file it converts that list and 
    returns a dictionary with correlated label and coordinate data.
    '''
    # Convert strings to ints and floats
    for i in range(0, len(list)):
        if len(list[i]) == 1:
            list[i] = int(float(list[i]))
        else:
            list[i] = float(list[i])
    # initialize variables        
    boxes = {'labels': [],
              'coords': []}
    i = -1
    neg_len = len(list) - (len(list) * 2)
    temp_list = []
    # Convert list to a functional dictionary of labels and coords
    while i >=  neg_len:
        if type(list[i]) == int:
            boxes['labels'].append(list[i])
            boxes['coords'].append(temp_list)
            temp_list = []
        else:
            temp_list.insert(0, list[i])
        i -= 1
    
    return boxes