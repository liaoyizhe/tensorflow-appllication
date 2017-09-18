# -*- coding: utf-8 -*-
from captcha.image import ImageCaptcha
import numpy as np
import matplotlib.pyplot as plt
# from config import NUMBER, CHAR_SMALL, CHAR_BIG, MAX_CAPTCHA, CHAR_SET_LEN, FONT_SIZE
import config
from PIL import Image
import random

# 生成随机的指定的字符串
def __gen_random_captcha_text(char_set=config.VALIDATE_STRING, size=None):
    # char_set必须为字符串
    if not char_set or not isinstance(char_set, str):
        raise ValueError('get the empty char_set')
    # 生成数组
    result = list(char_set)
    # 随机排序
    random.shuffle(result)
    # 返回字符串
    return ''.join(result[0:size])

#
def gen_random_captcha_image():
    # 定义图片属性
    image = ImageCaptcha(width=config.IMAGE_WIDTH, height=config.IMAGE_HEIGHT, font_sizes=[config.FONT_SIZE])
    text = __gen_random_captcha_text(size=config.MAX_CAPTCHA)
    # 生成验证码图片
    captcha = image.generate(text)
    # 打开并变为灰度图片
    captcha_image = Image.open(captcha).convert('L')
    # 将图片转换成二维数组
    captcha_source = np.array(captcha_image)
    return text, captcha_source

char_dict = {}

def prepare_char_dict():
    if char_dict:
        return char_dict

    for index, val in enumerate(config.VALIDATE_STRING):
        char_dict[val] = index

    return char_dict

# text, captcha_source = gen_random_captcha_image()
# print text
# print captcha_source.shape

# a = np.array([[[1,3],[2,4],[3,5]],[[1,3],[2,4],[3,5]]])
# b = a.flatten()
# c = np.zeros([2, 12])
# c[0:] = b
# c[1:] = b
# print c

print prepare_char_dict()