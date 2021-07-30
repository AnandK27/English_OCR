
# training
## prepare data
- First, download the pre-trained model of VGG net and put it in data/vgg_16.ckpt. you can download it from [tensorflow/models](https://github.com/tensorflow/models/tree/1af55e018eebce03fb61bba9959a04672536107d/research/slim)
- Second, download the dataset we prepared from [google drive](https://drive.google.com/file/d/1npxA_pcEvIa4c42rho1HgnfJ7tamThSy/view?usp=sharing) or [baidu yun](https://pan.baidu.com/s/1nbbCZwlHdgAI20_P9uw9LQ). put the downloaded data in data/dataset/mlt, then start the training.
- Also, you can prepare your own dataset according to the following steps. 
- Modify the DATA_FOLDER and OUTPUT in utils/prepare/split_label.py according to your dataset. And run split_label.py in the root
```shell
python ./utils/prepare/split_label.py
```
- it will generate the prepared data in data/dataset/
- The input file format demo of split_label.py can be found in [gt_img_859.txt](https://github.com/eragonruan/text-detection-ctpn/blob/banjin-dev/data/readme/gt_img_859.txt). And the output file of split_label.py is [img_859.txt](https://github.com/eragonruan/text-detection-ctpn/blob/banjin-dev/data/readme/img_859.txt). A demo image of the prepared data is shown below.


***
## train 
Simplely run
```shell
python ./main/train.py
```
- The model provided in checkpoints_mlt is trained on GTX1070 for 50k iters. It takes about 0.25s per iter. So it will takes about 3.5 hours to finished 50k iterations.
***

