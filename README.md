
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
	

Anomaly Detection and Visualization
========
First download and unzip `'train_pretrained_resnet50_features.zip'` in `'data'` file. Put the `'train_pretrained_resnet50_features.csv'` in the working directory and run `'Anomaly Detection.ipynb'`.
The output `'outlier_ind.csv'` and `'outlier_if_ind.csv'` are outlier indices for OCSVM and Isolation Forest respectively.

Next run `'outlier_if_ind.csv'`. Note that the data_directory need to be changed to the directory of original semi-conductor datasets accordingly.

Results
-------
Consider bad samples as positive cases.

Validation set AUC 0.9888
|tpr|fpr   |thr|
|---|------|---|
|1  |0.7964|0.00026|
|0.99|0.3014|0.00214|
|0.98|0.2468|0.00283|

Training set AUC 0.996
|tpr|fpr   |thr|
|---|------|---|
|1 |0.664|0.000493|
|0.99|0.083|0.00902|
|0.98|0.026|0.0398|

Test set AUC 0.989
|tpr|fpr|thr|
|---|---|---|
|1  |0.747|0.000336|
|0.99|0.179|0.00393|
|0.98|0.054|0.0141|

Class weight: 100 to 1

Validation set AUC 0.989

|tpr|fpr|thr|
|---|---|---|
|1|0.408|0.0185|
|0.99|0.300|0.0274|
|0.98|0.123|0.0685|

Training set AUC 0.997

|tpr|fpr|thr|
|---|---|---|
|1|0.637|0.00909|
|0.99|0.0235|0.696|
|0.98|0.016|0.918|


Test set AUC 0.982

|tpr|fpr|thr|
|---|---|---|
|1|0.629|0.00913|
|0.99|0.410|0.0195|
|0.98|0.265|0.0327|

Filtered dataset(AUC 0.9891)
Validation set
|tpr|fpr|
|---|---|
|1 | 0.8842|
|0.99|0.2394|
|0.98|0.1420|

Augmented 10k more bad images still 14 epoch training 
|tpr|fpr|
|---|---|
|1  |0.957|
|0.99|0.4286|
|0.98|0.0834|
