import sys
import os
from deep_privacy_anonymize import anon_and_write_imgs
import gc
print('----> driver \t- args received:',sys.argv)
from flask import jsonify
_ , filepath_upload , filepath_public = sys.argv

print('----> driver \t- filepath_public',filepath_public)
print('----> driver \t- filepath_upload',filepath_upload)
print('----> driver \t- calling anonymizer')

path_to_ckpt = './deep_privacy/resources/cpu_checkpoint.ckpt'
anon_and_write_imgs([filepath_upload],[filepath_public])

print('---> driver \t- anonymizer done')
print('---> driver \t- collecting garbage')
gc.collect()
print('---> driver \t- terminating')
