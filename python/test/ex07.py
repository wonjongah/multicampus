from PIL import Image, ImageFilter
im = Image.open('cute_cat.jpg')
blurImage = im.filter(ImageFilter.BLUR)
blurImage.save('cute_cat_blur.png')
# 선명하면 눈엔 좋은데, 컴이 처리하기 더 안 좋다, 살짝 흐릿하게 해줌
blurImage.show()

# 다른 필터 궁금하면 pillow 도큐먼트 보면 된다