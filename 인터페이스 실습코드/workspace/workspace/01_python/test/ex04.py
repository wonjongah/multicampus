from PIL import Image

# 사각형 나타내는 정보, 좌측상단, 우측하단 좌표
# 좌측상단의 좌표와 폭과 높이 주는 것
im = Image.open("cute_cat.jpg")
cropImage = im.crop((100, 100, 150, 150)) # (좌, 상, 우, 하)
cropImage.save('cute_cat_crop.jpg')
cropImage.show()


# 번호판, 혹은 얼굴 크롭할 때 쓰임

# 정사각형 가운데 추출하고 싶다아 센터크롭..
