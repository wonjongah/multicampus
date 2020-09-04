from PIL import Image
im = Image.open('cute_cat.jpg')
print(im.size)
# 크기를 600x600 으로
img2 = im.resize((600, 600))  # 가로세로 무시하고 이 사이즈에 맞춤
img2.save('cute_cat_600.jpg')
img2.show()
# 90도 회전
img3 = im.rotate(-90)   # 양수는 반시계, 시계방향은 음수!!!
img3.save('cute_cat_rotate.jpg')
img3.show()
print(img3.size)  # 크기는 그대로, 나머지는 검정색 디폴트