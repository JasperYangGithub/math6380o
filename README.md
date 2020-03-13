
The original dataset downloaded from Kaggle has 27,000 good samples and 3,000 bad samples.
After splitting the training and validation datasets, we did data augmentation to compensate the minority of bad samples.
After augmentation by `data/image_transformation.py` by setting N=13033, the total training set has 40,000 images.

The following table displays the number of images in the training and validation datasets.
|        |train | val  |total|
|--------|------|------|-----|
|good    |24289 | 2711 |27000|
|bad     | 2678 |  322 | 3000|
|augbad  |13033 |      |     |
|total   |40000 | 3033 |     |

Prepare dataset
=======

To prepare dataset, download the original data from https://www.kaggle.com/c/semi-conductor-image-classification-first/data
Download `data/val_bads.csv`, `data/val_goods.csv`, `data/split_val.py`
into the same directory. In this directory, run
`python split_val.py path/to/dataset/dir`
in the command line window, to separate a validation set named path/to/dataset/dir/val from images in path/to/dataset/dir/train.

Simple augmented dataset
-------------
To augment the data, run
`python path/to/dir/image_transformation.py path/to/dataset/dir/train/bad_1 13033`
to generate 13033 additional bad images in the training set. 

Filtered dataset
-------------
Later we tried the dataset after filtering, though we didn't find that it improve the result.
Download `data/train_normal_bads.csv`, `data/train_normal_goods.csv` and `data/filtered_dataset.sh`
In the linux command line window, run
```
chmod 755 filtered_dataset.sh
./filtered_dataset.sh path/to/dataset/dir path/to/new/dataset/dir path/to/dir/train_normal_goods.csv path/to/dir/train_normal_bads.csv
```
to create a new dataset under directory path/to/new/dataset/dir


Training
========
Training is done by transfer learning. 
* Find training using Resnet18, 50, EfficientNet on simple augmented dataset and Resnet 50 on filtered dataset in `Transferlearning_Resnet_EfficientNet.ipynb`
Note `dataset_dir= 'path/to/dataset/dir'` is by default `'kaggle_data'`. Please change it to your dataset directory.
* Find training using Wide Resnet50-2, Resnet50-32X4d in `Resnet.ipynb` 


The code for test models, feature extraction, and heatmap plotting using class activation mapping is in `Test_featureExtract_heatmap.ipynb`.
	
Results
-------
Consider bad samples as positive cases.
|tpr|fpr   |
|---|------|
|1  |0.7964|
|0.99|0.3014|
|0.98|0.2468|


