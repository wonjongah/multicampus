from PIL import Image
def center_crop(im): # 가운데 크롭, 적은 길이가 정사각형의 길이
     crop_size = min(im.size)
     left = (im.size[0] - crop_size)//2  # 잘라내야 할 양쪽의 좌표를 찾아내는 것
     top = (im.size[1] - crop_size)//2
     right = (im.size[0] + crop_size)//2
     bottom = (im.size[1] + crop_size)//2
     return im.crop((left, top, right, bottom))  # crop은 튜플을 매개변수로 받아서
im = Image.open('cute_cat.jpg')
cropImage = center_crop(im)
cropImage.save('cute_cat_center_crop.jpg')
cropImage.show()

# 근디 작은 길이로 자르면 정보손실이 있음, 대신 긴 길이로 정사각형 만들면 정보손실이 일어나지 않음
# 남은 영역은 흰 색으로 채움
# 그 위치에 덮어쓰기?
