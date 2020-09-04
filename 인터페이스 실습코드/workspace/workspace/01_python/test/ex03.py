from PIL import Image

im = Image.open("cute_cat.jpg")

size = (64,64)
im.thumbnail(size)  # 원본 바꾼다, 새로운 이미지 리턴이었으면 왼쪽에 받아주는 변수 있었을 것
# 가로세로 비율 맞추면서, 긴 쪽의 길이를 맞춘다
im.save("cute_cat_thumb.jpg")
im.show()

print(im.size)