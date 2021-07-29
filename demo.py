import os
from ocr import ocr
import time
import shutil
import numpy as np
from PIL import Image
from glob import glob
import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import rotate

from deskew import determine_skew
import cv2



def resize_image(img):
    img_size = img.shape
    im_size_min = np.min(img_size[0:2])
    im_size_max = np.max(img_size[0:2])

    im_scale = float(600) / float(im_size_min)
    if np.round(im_scale * im_size_max) > 1200:
        im_scale = float(1200) / float(im_size_max)
    new_h = int(img_size[0] * im_scale)
    new_w = int(img_size[1] * im_scale)

    new_h = new_h if new_h // 16 == 0 else (new_h // 16 + 1) * 16
    new_w = new_w if new_w // 16 == 0 else (new_w // 16 + 1) * 16

    re_im = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
    return re_im, (new_h / img_size[0], new_w / img_size[1])

def single_pic_proc(image_file):
    image = np.array(Image.open(image_file).convert('RGB'))
    image, (rh, rw) = resize_image(image)
    # grayscale = rgb2gray(image)
    # angle = determine_skew(grayscale)
    # rotated = rotate(image, angle, resize=True) * 255
    # image = rotated.astype(np.uint8)
    result = ocr(image,image_file)
    return result


if __name__ == '__main__':
    image_files = os.listdir('./test_images/')
    image_files = [os.path.join('./test_images/',f) for f in image_files]
    result_dir = './test_result/'
    results_dir = './test_result/test_images/'
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    
    os.mkdir(results_dir)

    for image_file in sorted(image_files):
        t = time.time()
        result = single_pic_proc(image_file)
        output_file = os.path.join(result_dir, image_file.split('/')[-1])
        print(output_file)
        txt_file = os.path.join(result_dir, image_file.split('/')[-1].split('.')[0]+'.txt')
        print(txt_file)
        txt_f = open(txt_file, 'w',encoding="utf-8")
        #Image.fromarray(image_framed).save(output_file)
        print("Mission complete, it took {:.3f}s".format(time.time() - t))
        print("\nRecognition Result:\n")
        for key in result:
            print(result[key][1])
            txt_f.write(result[key][1]+'\n')
        txt_f.close()