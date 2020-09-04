from django.db import models
# 모델클래스 정의 django.db.models.Model을 상속 받아 정의
class Bookmark(models.Model): # 장고의 모델 클래스 상속받겠다
    # 생성자 정의 안 했는데? 그럼 디폴트 생성자 쓰겠다~
    # self. 어쩌구 없음.. 
    title = models.CharField('TITLE', max_length=100, blank=True) # 클래스 변수, 클래스 당 하나!
    # char 쓸 때는 max_length 필수!
    #컬럼이름 = 타입 (사람을 위한 정의.. 공백 허용할 거냐(sql용어 null) false면 not null)
    url = models.URLField('URL', unique=True)  # 모든 인스턴스가 공유해서 쓰는 것, cls.뭐뭐 이렇게 접근
    # 인스턴스의 정보가 아니라 클래스 차원에서 관리하는 정보
    # 테이블의 컬럼과 매칭되는 것
    # unique -> 중복허용하지 않겠다

    # 프라이머리키 지정 안 하면 자동으로 id integer auto_increment primary key가 자동으로 들어감
    # 그래서 총 세 개 만들어짐 title url id

    # create table Bookmark(
    # title varchar(100) null,
    # url varchar(...) unique); 이 문장을 위처럼 표기한 것
    def __str__(self):
        return self.title


# Create your models here.
