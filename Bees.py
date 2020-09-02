import os

# Create directory
import shutil

original_dataset_dir = 'kaggle_bee_vs_wasp'
# Create target Directory if don't exist
if not os.path.exists(original_dataset_dir):
    os.mkdir(original_dataset_dir)
    print("Directory " , original_dataset_dir ,  " Created ")
else:
    print("Directory " , original_dataset_dir ,  " already exists")


dirName = 'bees&wasps/train/bees'
# Create target directory & all intermediate directories if don't exists
try:
    os.makedirs(dirName)
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")


dirName = 'bees&wasps/train/wasps'
# Create target directory & all intermediate directories if don't exists
try:
    os.makedirs(dirName)
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

dirName = 'bees&wasps/train/wasps'
# Create target directory & all intermediate directories if don't exists
try:
    os.makedirs(dirName)
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

dirName = 'kaggle_bee_vs_wasp/bee1'
# Create target directory & all intermediate directories if don't exists
try:
    os.makedirs(dirName)
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

dirName = 'bees&wasps/test/bees'
# Create target directory & all intermediate directories if don't exists
try:
    os.makedirs(dirName)
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")


dirName = 'bees&wasps/test/wasps'
# Create target directory & all intermediate directories if don't exists
try:
    os.makedirs(dirName)
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

dirName = 'bees&wasps/validation/bees'
# Create target directory & all intermediate directories if don't exists
try:
    os.makedirs(dirName)
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")


dirName = 'bees&wasps/validation/wasps'
# Create target directory & all intermediate directories if don't exists
try:
    os.makedirs(dirName)
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

    import os
    from shutil import copy

dir_src = r"C:\\Users\\Mirela\\PycharmProjects\\Bee\\kaggle_bee_vs_wasp\\bee1"
dir_dst = r"C:\\Users\\Mirela\\PycharmProjects\\Bee\\bees&wasps\\train\\bees"

files = ['bee1.{}.jpg'.format(i) for i in range(1000)]
for root, _, files in os.walk(dir_src):
        for file in files:
            if file.endswith('.jpg'):
                copy(os.path.join(root, file), dir_dst)

dir_src = r"C:\\Users\\Mirela\\PycharmProjects\\Bee\\kaggle_bee_vs_wasp\\bee1"
dir_dst = r"C:\\Users\\Mirela\\PycharmProjects\\Bee\\bees&wasps\\validation\\bees"

files = ['bee1.{}.jpg'.format(i) for i in range(1000,1500)]
for root, _, files in os.walk(dir_src):
        for file in files:
            if file.endswith('.jpg'):
                copy(os.path.join(root, file), dir_dst)

dir_src = r"C:\\Users\\Mirela\\PycharmProjects\\Bee\\kaggle_bee_vs_wasp\\bee1"
dir_dst = r"C:\\Users\\Mirela\\PycharmProjects\\Bee\\bees&wasps\\test\\bees"

files = ['bee1.{}.jpg'.format(i) for i in range(1000,1500)]
for root, _, files in os.walk(dir_src):
        for file in files:
            if file.endswith('.jpg'):
                copy(os.path.join(root, file), dir_dst)


