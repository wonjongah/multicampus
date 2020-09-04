from django.contrib import admin
# Register your models here.
from bookmark.models import Bookmark  # 북마크 모델을 북마크로 임포트하겠다

@admin.register(Bookmark)  # 이 클래스의 모델로 Bookmark를 쓴다
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url') # 사이트에서 출력할 컬럼 목록
    # 뭘 보여줄 거냐~ 이 세개의 컬럼 보여주겠다
