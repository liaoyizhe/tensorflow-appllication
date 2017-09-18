# -*- coding: utf-8 -*-

from captcha.image import ImageCaptcha
import numpy as np
import matplotlib.pyplot as plt
# from config import NUMBER, CHAR_SMALL, CHAR_BIG, MAX_CAPTCHA, CHAR_SET_LEN, FONT_SIZE
import config
from PIL import Image
import random

char_dict = {}
number_dict = {}


# 生成随机的指定的字符串
def __gen_random_captcha_text(char_set=config.VALIDATE_STRING, size=None):
    # char_set必须为字符串
    if not char_set or not isinstance(char_set, str):
        raise ValueError('get the empty char_set')
    # 生成字符串数组
    result = list(char_set)
    # 打散自字符串
    random.shuffle(result)
    # 返回字符串
    return ''.join(result[0:size])

# 生成验证码图片
def gen_random_captcha_image():
    # 定义图片属性
    image = ImageCaptcha(width=config.IMAGE_WIDTH, height=config.IMAGE_HEIGHT, font_sizes=[config.FONT_SIZE])
    text = __gen_random_captcha_text(size=config.MAX_CAPTCHA)
    # 生成验证码图片
    captcha = image.generate(text)
    captcha_image = Image.open(captcha)
    # 将图片转换成三维数组 shape是(60,160,3)
    captcha_source = np.array(captcha_image)
    # print captcha_source.shape
    return text, captcha_source


# always gen the require image height ,and width image
def gen_require_captcha_image():
    while 1:
        text, image = gen_random_captcha_image()
        if image.shape == (config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 3):
            return text, image

# 返回key=>value数组,key=字符,value=所表示的数字
# prepare the char to index
def prepare_char_dict():
    if char_dict:
        return char_dict

    for index, val in enumerate(config.VALIDATE_STRING):
        char_dict[val] = index

    return char_dict

def prepare_number_dict():
    if number_dict:
        return number_dict

    for index, val in enumerate(config.VALIDATE_STRING):
        number_dict[index] = val

    return number_dict

# 将字符串text转换成长度为config.MAX_CAPTCHA * config.CHAR_SET_LEN的整形数组,每一段以config.CHAR_SET_LEN为单位,代表一个字符
def text_to_array(text):
    char_dict_tmp = prepare_char_dict()

    arr = np.zeros(config.MAX_CAPTCHA * config.CHAR_SET_LEN, dtype=np.int8)
    for i, p in enumerate(text):
        key_index = char_dict_tmp[p]
        index = i * config.CHAR_SET_LEN + key_index
        arr[index] = 1

    return arr

# 同理,将字符数组转换为字符串
def array_to_text(arr):
    num_dict_tmp = prepare_number_dict()
    text = []
    char_pos = arr.nonzero()[0]
    for index, val in enumerate(char_pos):
        if index == 0:
            index = 1
        key_index = val % (index * config.CHAR_SET_LEN)
        text.append(num_dict_tmp[key_index])
    return ''.join(text)


def show_image_text():
    text, image = gen_random_captcha_image()

    f = plt.figure()
    ax = f.add_subplot(111)
    ax.text(0.1, 0.9, text, ha='center', va='center', transform=ax.transAxes)
    plt.imshow(image)

    plt.show()


#
if __name__ == '__main__':
    # __do_image_text()
    # arr = text_to_array('0142')
    # print '==========='
    # print array_to_text(arr)
    show_image_text()
