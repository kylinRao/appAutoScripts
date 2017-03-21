# coding=utf-8
from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open('fengZhuanFu.png').convert('L'))
print im.shape
print im

# Sobel 导数滤波器
imx = zeros(im.shape)
print imx
filters.sobel(im,1,imx)

imy = zeros(im.shape)
filters.sobel(im,0,imy)

magnitude = sqrt(imx**2+imy**2)