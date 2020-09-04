from PIL import Image
import numpy as np
im = Image.open('cute_cat.jpg')
# Image --> numpy array
im2arr = np.array(im) # im2arr.shape: height x width x channel(channel => rgb 각각 어떻게 되나)
    #(3차원데이터)
    #이미지의 색상정보만 받아와 변환시켜주는 것!
    #리스트처럼 차원을 가지고 관리해줌
    #numpy!!!!!!!!픽셀단위로 작업할 때 필요
# numpy array --> Image
print(im2arr.shape)
print()
print(im2arr)
arr2im = Image.fromarray(im2arr) # 픽셀들을 이미지 객체로 만듦
arr2im.show()