class Date:
     def __init__(self, month):
         self.inner_month = month

     @property    # @property함수는 같은 이름의 함수 지정 가능
     def month(self):
         return self.inner_month

     @month.setter
     def month(self, month):
         if 1 <= month <= 12:
            self.inner_month = month

today = Date(8)
today.month = 15
# today.inner_month = 15  => @property 아님!! 그냥 필드변수, 그래서 잘못된 값을 가지게 된다..
# @property 쓰면 실수나 잘못된 사용 예방할 수 있다
print(today.month)