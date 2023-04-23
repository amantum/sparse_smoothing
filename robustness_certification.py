import math
from datetime import datetime
import io
import sys
import argparse
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import torch

from sparse_smoothing.cert import binary_certificate_grid

parser = argparse.ArgumentParser()

parser.add_argument('--file', type=str, required=True, help=\
'Path to the file contating info about smooth probabilities')

parser.add_argument('--pp', type=float, required=False, help=\
'Probability of fliping 0 to 1; values in the file will be replaced \
with this if provided')

parser.add_argument('--pm', type=float, required=False, help=\
'Probability of fliping 1 to 0; values in the file will be replaced \
with this if provided')

parser.add_argument('--ra', type=int, default=5, help=\
'Maximum addition radius to certify against')

parser.add_argument('--rd', type=int, default=5, help=\
'Maximum deletion radius to certify against')

args = parser.parse_args()

file_name =  args.file

p_plus = args.pp
p_minus = args.pm

ra = args.ra
rd = args.rd

sys.exit()

print(f'Reading from smooth_classifier_metadata from {file_name}')
    
with open(file_name, 'r') as fp:
    smooth_classifier_meta_data = json.load(fp)

y_smooth = smooth_classifier_meta_data['y_smooth']

if p_plus is None:
    p_plus = y_smooth['p_plus'] 

if p_minus is None:
    p_minus = y_smooth['p_minus'] 

print(f'Using p_plus = {p_plus} and p_minus = {p_minus}')

grid_binary_class, *_ = \
binary_certificate_grid(pf_plus=p_plus, pf_minus=p_minus, \
max_ra=ra, max_rd=rd, \
p_emps=y_smooth, reverse=False, progress_bar=True)



