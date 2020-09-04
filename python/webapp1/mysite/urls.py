"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookmark.views import BookmarkLV, BookmarkDV
# from bookmark.views import index, detail
from mysite.views import HomeView
from django.conf import settings
from django.conf.urls.static import static
from mysite.views import HomeView, UserCreateView, UserCreateDoneTV


urlpatterns = [

    # 회원 가입 및 처리
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(),name='register_done'),
    # 로그인, 로그아웃, 비밀번호 변경 등 담당
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),

    # class-based views 클래스기반뷰!!!!!!!!!!!!!!!!!!!!!!
    # http//127.0.0.1:8000/bookmark이거 하면 리스트뷰에게 처리해!
    # model.object.all()해서 리턴받는다!
    # 그 목록을 컨텍스트 변수 object_list에 담아서 렌더링......
    # 만들어졌으면 브라우저에게 보냄
    #     path('bookmark/', BookmarkLV.as_view(), name='index'),
    #사용할 url, 이 url을 처리할 뷰가 누구냐
    #     path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'),
    # bookmark/보고 싶은 북마크의 아이디값(매번 바뀌는 값) 어떤 의미로 변수
    # path 속 변수라고 해서 (path variable)경로변수라고 불림.... /book/id
    # <>표기를 꺽세로.. <>만나면 경로변수다!! :을 기준으로 왼이 데이터 타입
    # 북마크 모델의 아이디타입이 인트!
    # : 오른쪽은 pk (프라이머리키) ****************중요 ****************
    # 꺼낼 정보 어디에 담겨있냐 <int:pk>로 들어감.... get(id=)이 값이!!
    #
    #함수기반!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # path('bookmark/', index, name='index'),
    # path('bookmark/<int:pk>', detail, name='detail'),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)