import sys
import io
from deep_privacy.config_parser import load_config
from deep_privacy.inference import infer, deep_privacy_anonymizer
import torch
import errno
import os


print('---> anony \t- checking resources')
path_to_pth = './deep_privacy/resources/WIDERFace_DSFD_RES152.pth'
path_to_ckpt = './deep_privacy/resources/cpu_checkpoint.ckpt'

if not os.path.exists(path_to_pth):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path_to_pth)

if not os.path.exists(path_to_ckpt):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path_to_ckpt)


def anon_and_write_imgs(list_of_path_to_imgs,list_of_path_to_saveimgs):
    print('---> anony \t- loading config')
    config = load_config("models/large/config.yml")
    print('---> anony \t- initializating generator')
    generator = infer.init_generator(config,torch.load(path_to_ckpt))
    print('---> anony \t- build anonymizer')

    anonymizer = deep_privacy_anonymizer.DeepPrivacyAnonymizer(generator,
                                                               batch_size=32,
                                                               use_static_z=True,
                                                               keypoint_threshold=.1,
                                                               face_threshold=.6)

    print('---> anony \t- anonymize')
    anonymizer.anonymize_image_paths(list_of_path_to_imgs, list_of_path_to_saveimgs)
