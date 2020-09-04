from PIL import Image # Image -> 클래스, 대문자로 시작, 스태틱메소드(생성 안 하고 바로 호출), 팩토리함수, 객체의 생성 과정 쉽게

# open image
im = Image.open("cute_cat.jpg")  # 이미지객체의 인스턴스 = im

print(im.size)

im.save("cute_cat.png")   # png로 저장

im.show()
