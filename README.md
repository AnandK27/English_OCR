# English_OCR
 
Dewarping done using [page_dewarp](https://github.com/mzucker/page_dewarp) <br>
Text detection is based on CTPN and is done using tensorflow.<br>
Text recognition is based CRNN and is done using pytorch. <br>

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

### Train
Train [CTPN](./detector/README.md) 
***

## Recognition (CRNN)
Recognition is based on [CRNN](http://arxiv.org/abs/1507.05717), some codes are borrowed from
[crnn.pytorch](https://github.com/meijieru/crnn.pytorch)

### Setup

Download pretrained models from [Baidu Netdisk](https://pan.baidu.com/s/1yllO9hBF8TgChHJ7i3WobA) (extract code: u2ff) or [Google Drive](https://drive.google.com/open?id=1hRr9v9ky4VGygToFjLD9Cd-9xan43qID)
and put these files into checkpoints.


### Train 
Train [CRNN](./train_code/train_crnn/readme.md)  
***

# Test
Place the test images in ./page_dewarp/example_input<br>
To test the data run the script file "run.sh"<br>
```shell
./run.sh
```
The text file will be generated in ./test_result
