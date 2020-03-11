# To be used within the same directory containing 'val_goods.csv' and 'val_bads.csv'
# create a subdirectory under the dataset directory parallel to 'train' named 'val' and subsubdirectories 'good_0', 'bad_1' under it.
import pandas as pd
import os
import sys
my_dir = sys.argv[1]
my_val = os.path.join(my_dir, 'val')
my_good = os.path.join(my_val, 'good_0')
my_bad = os.path.join(my_val, 'bad_1')
try: 
    os.mkdir(my_val) 
except OSError as error: 
    print(error)
try: 
    os.mkdir(my_good) 
except OSError as error: 
    print(error)
try: 
    os.mkdir(my_bad) 
except OSError as error: 
    print(error)
    
goodImageNames = pd.read_csv('val_goods.csv', index_col=False, header=None)
goodnames = goodImageNames[0].values
for i in goodnames:
    os.rename(os.path.join(my_dir, 'train','good_0', i), os.path.join(my_good,i))

    
badImageNames = pd.read_csv('val_bads.csv', index_col=False, header=None)
badnames = badImageNames[0].values
for i in badnames:
    os.rename(os.path.join(my_dir, 'train', 'bad_1', i), os.path.join(my_bad,i))

