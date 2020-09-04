from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # where절과 비슷
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    # 이 세 개만 보여달라~ 눈에 보이게
    list_filter = ('modify_dt',)
    # 필터링하겠다, 오른쪽 보면 날짜 기준으로 필터링할 수 있는 모디파이 데이트 생겼을 것
    search_fields = ('title', 'content')
    # 맨 위에 보면 서치, 서치 대상이 되는 컬럼명을 주는 것 검색 누르면, 타이틀과 컨텐트 파트에서 검색
    prepopulated_fields = {'slug': ('title',)}


    def get_queryset(self, request):
          return super().get_queryset(request).prefetch_related('tags')


    def tag_list(self, obj):
          return ', '.join(o.name for o in obj.tags.all())
