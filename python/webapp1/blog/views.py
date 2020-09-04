from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView
from blog.models import Post

from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, \
    TodayArchiveView

from django.views.generic import FormView
from django.db.models import Q
from django.shortcuts import render
from blog.forms import PostSearchForm


# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'  # 템플릿 파일명 변경
    # 앱이름_list.html이 디폴트인데 이름 바꾸겠다

    context_object_name = 'posts'  # 컨텍스트 객체 이름 변경(object_list)

    # 가독성을 좋게 하기 위해 오브젝츠 리스트를 포스츠로 바꿀 것이다

    paginate_by = 3  # 페이지네이션, 페이지당 문서 건 수
    # 한 페이지 당 보여줄 데이터 건수


# DetailView
class PostDV(DetailView):
    model = Post
    context_object_name = 'post'  # 오브젝츠 대신에 포스트로!!!


# ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True  # 목록도 가지겠다


# 오브젝트리스트가 안 넘어온다 이거 설정 안 하면, 글 목록도 보여주고자하면 오브젝트리스트 트루로
# 이거 주석처리하면 년도로 모은 곳에서 리스트 안 나옴
class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'  # 숫자로 된 월로 포맷하겠다


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    # 데이터필드를 모디파이로 정해놔서 이걸로
    month_format = '%m'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'  # 디폴트가 문자열로 된 월 명칭 %b

    # --- Tag View


class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context


# --- FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        # self, form => forms의form
        # 이게 호출됐다, 유효성 검사에 성공! 실패시 이거 호출은 커녕 폼으로 돌아감
        searchWord = form.cleaned_data['search_word']
        # cleaned_data => 유효성 검사 끝난 데이터 들어있음(사전)
        post_list = Post.objects.filter(
            # title like serchword 이 단어 포함하고 있냐
            # sql에서 title like '%searchword%'과 같다오
            Q(title__icontains=searchWord) |
            # | or 타이틀에 있거나 ~컨텐트에 있거나~
            Q(description__icontains=searchWord) |
            Q(content__icontains=searchWord)
        ).distinct()
        context = {}
        # 컨텍스트 변수 구성중~ 부모 이용하지 않고.. 비어있는 사전 만들고, 이름가지고 하나하나 넣음
        context['form'] = form  # form은 매개변수로 전달된 녀석, 실제로는 postseachform의 매개변수
        context['search_term'] = searchWord
        context['object_list'] = post_list
        return render(self.request, self.template_name, context)
    # 렌더로 직접 호출
