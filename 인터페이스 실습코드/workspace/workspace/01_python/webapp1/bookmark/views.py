from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
# 부모클래스로 리스트뷰(목록보겠다)랑 디테일뷰(한 개를 자세히 보겠다)
from bookmark.models import Bookmark




class BookmarkLV(ListView):
    model = Bookmark  # 클래스변수 self.아님
    #이 뷰가 사용할 모델이 뭐냐? 북마크 사용할 거임
    context_object_name = 'bookmark_list'

class BookmarkDV(DetailView):  # BookmarkDV는 디테일뷰의 닉네임
    model = Bookmark
    context_object_name = 'bookmark'
#
# def index(request):
#     # request 웹브라우저가 전송한 것이 담겨있음
#     # request로 어떤 내용이 전달됐나도 확인할 수 있음
#     object_list = Bookmark.objects.all()
#     # Bookmark는 부모클래스가 정할 수 없음, 모델객체, 어떤 모델객체를 쓸 것인가
#     # 그래서 자식클래스에서 모델을 지정하는 게 필수임
#     # class BookmarkDV(DetailView):  # BookmarkDV는 디테일뷰의 닉네임
#     #     model = Bookmark  <---- 이거!!!
#
#     print(object_list)
#     # 콘솔에 한 번 출력해보겠다
#     context = {'bookmark_list': object_list}
#     # 사전 하나 만들 것, 이름은 컨텍스트 오브젝트리스트라는 키로 오브젝트리스트 조회
#     return render(request, 'bookmark/bookmark_list.html', context)
#     # 렌더로 템플릿 전달, 렌더의 리턴값을 브라우저가 받게 되는 것
#     # 두 번째 인자가 템플릿 경로, 템플릿츠 디렉토리는 고정! 그 밑에 북마크 밑에 북리스트.html
#     # 이 파일로 템플릿 쓰겠다
#     # 컨텍스트에 사전 전달하면 렌더가 변수명과 변수값을 바꾸어서 지정해줌
#     # 이렇게 넘어갔기 때문에 html에서 object_list로 루프 돌리는 것
#     # 리스폰스.................
#
#
#     #path variable의 이름과 같아야 함, 두 번째 인자
# def detail(request, pk):
#     object = Bookmark.objects.get(pk=pk)    # .get(id=pk)
#     context = {'bookmark': object}
#     return render(request, 'bookmark/bookmark_detail.html', context)