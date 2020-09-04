from PIL import Image


im = Image.open("cute_cat.jpg").convert("L")
# open의 리턴값 이미지
# convert : "L" (gray), "RGB", "RGBA(A=투명도)", "CMYK"
im.show()