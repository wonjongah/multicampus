from django.urls import path, re_path
from blog.views import *  # 임포트에 views라고 했으면 views.~ 이렇게 써야 하는디 *이니까 이름으로 바로
# from blog import views

app_name = 'blog'

urlpatterns = [
 # Example: /blog/
 path('', PostLV.as_view(), name='index'),
 # Example: /blog/post
 path('post/', PostLV.as_view(), name='index'),

 re_path(r'^post(?P<slug>[-\w]+)/$', PostDV.as_view(), name='detail'),

 # Example: /blog/archive/
 path('archive/', PostAV.as_view(), name='post_archive'), # ㅡㅡ 위의 애랑 겹쳐서 위의 PostDv가 가로챈 것, 안 겹치게 /archive
 # Example: /blog/archive/2019/
 path('archive/<int:year>/', PostYAV.as_view(), name='post_year_archive'),
 # Example: /blog/archive/2019/nov/
 path('archive/<int:year>/<str:month>/', PostMAV.as_view(), name='post_month_archive'),
 # Example: /blog/archive/2019/nov/10/
 path('archive/<int:year>/<str:month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'),
 # Example: /blog/archive/today/
 path('archive/today/', PostTAV.as_view(), name='post_today_archive'),

 # Example: /blog/tag/
 path('tag/', TagCloudTV.as_view(), name='tag_cloud'),
 # Example: /blog/tag/tagname/
 path('tag/<str:tag>/', TaggedObjectLV.as_view(), name='tagged_object_list'),
 # Example: /blog/search/
 path('search/', SearchFormView.as_view(), name='search'),

]

# re -> 정규표현식, 문자를 표현하는
# r'^(?P<slug>[-\w]+)/$' => r하고 나옴
# regular expression
# ^이걸로 시작해서 $이걸로 끝난다
# (안의 .은) 글자 하나, 글자 0개 이상 나온다
# ex)  ^h(.)*s$  => has hs htttts attx는 틀림
# P<slug> 꺾세 경로변수, 슬러그라는 이름의 경로변수를 지정
# w는 워드, 알파벳과 숫자
# +이런 것들이 한 개 이상 나온다
# 즉!!!!! 공백없이 글자, 숫자, -로만 허용한다!!!!!! 그리고 마지막에 /로 끝나야 한다!!!!!
# 그걸 슬러그로 받겠다