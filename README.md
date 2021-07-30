# English_OCR
   
Text detection is based on CTPN and is done using tensorflow 
Text recognition is based CRNN and is done using pytorch. 

## Prerequisite

- python
- pytorch
- torchvision
- tensorflow
- opencv
- numpy


They could all be installed through pip except pytorch and torchvision. As for pytorch and torchvision, 
they both depends on your CUDA version, you would prefer to reading [pytorch's official site](https://pytorch.org/)


## Detection (CTPN)
Detection is based on [CTPN](https://arxiv.org/abs/1609.03605). It is implemented in tensorflow. Also, the original code can be found in [here](https://github.com/eragonruan/text-detection-ctpn/tree/banjin-dev). 


### Setup
- download the ckpt file from [googl drive](https://drive.google.com/file/d/1HcZuB_MHqsKhKEKpfF1pEU85CYy4OlWO/view?usp=sharing)
- put checkpoints_mlt/ in detector/text-detection-ctpn/

```shell
python ./main/demo.py
```
***
### training
Train [CTPN](./detector/readme.md) 
#### prepare data
- First, download the pre-trained model of VGG net and put it in data/vgg_16.ckpt. you can download it from [tensorflow/models](https://github.com/tensorflow/models/tree/1af55e018eebce03fb61bba9959a04672536107d/research/slim)
- Second, download the dataset we prepared from [google drive](https://drive.google.com/file/d/1npxA_pcEvIa4c42rho1HgnfJ7tamThSy/view?usp=sharing) or [baidu yun](https://pan.baidu.com/s/1nbbCZwlHdgAI20_P9uw9LQ). put the downloaded data in data/dataset/mlt, then start the training.
- Also, you can prepare your own dataset according to the following steps. 
- Modify the DATA_FOLDER and OUTPUT in utils/prepare/split_label.py according to your dataset. And run split_label.py in the root
```shell
python ./utils/prepare/split_label.py
```
- it will generate the prepared data in data/dataset/
- The input file format demo of split_label.py can be found in [gt_img_859.txt](https://github.com/eragonruan/text-detection-ctpn/blob/banjin-dev/data/readme/gt_img_859.txt). And the output file of split_label.py is [img_859.txt](https://github.com/eragonruan/text-detection-ctpn/blob/banjin-dev/data/readme/img_859.txt). A demo image of the prepared data is shown below.
<img src="/data/readme/demo_split.png" width=640 height=480 />

***
### train 
Simplely run
```shell
python ./main/train.py
```
- The model provided in checkpoints_mlt is trained on GTX1070 for 50k iters. It takes about 0.25s per iter. So it will takes about 3.5 hours to finished 50k iterations.
***

## Recognition (CRNN)
Recognition is based on [CRNN](http://arxiv.org/abs/1507.05717), some codes are borrowed from
[crnn.pytorch](https://github.com/meijieru/crnn.pytorch)

### Setup

Download pretrained models from [Baidu Netdisk](https://pan.baidu.com/s/1yllO9hBF8TgChHJ7i3WobA) (extract code: u2ff) or [Google Drive](https://drive.google.com/open?id=1hRr9v9ky4VGygToFjLD9Cd-9xan43qID)
and put these files into checkpoints.


### Train 
Train [CRNN](./train_code/train_crnn/readme.md)  

## Test
Place the test images in ./test_images
To test the data run the script file "run.sh"
```shell
./run.sh
```
The text file will be generated in ./test_result
