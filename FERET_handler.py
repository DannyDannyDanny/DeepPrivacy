import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob

# all images in FERET subdirs
img_paths = glob.glob('../FERET/originals/*.png')

# list of Person IDentification (PID)-numbers
pid_list = [int(i.split('_')[0].split('/')[-1]) for i in img_paths]

# lookup images for a given PID
def pid_imgs_lookup(pid):
    return [i for i in img_paths if int(i.split('_')[0].split('/')[-1]) == pid]

# Dict with Key: pid - Value: list of image-paths
pid_dict = {pid:pid_imgs_lookup(pid) for pid in pid_list}

# %% Anonymize all photos
import sys
import os
from deep_privacy_anonymize import anon_and_write_imgs

batch_size = 30
# number of faces to anonymize at once
for i in range(0,len(img_paths),step_size):
    print('anonymizing:',i,i+step_size-1)
    filepath_original = img_paths[i:i+step_size-1]
    filepath_anonymized = [i.replace('originals','anonymized') for i in filepath_original]
    anon_and_write_imgs(filepath_original,filepath_anonymized)
# %%

for path_img in pid_dict[223]:
    print(path_img)
    img = mpimg.imread(path_img)
    plt.imshow(img)
    plt.show()

# %%
