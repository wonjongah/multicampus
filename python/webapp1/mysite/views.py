from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# 순수하게 html 템플릿만 운영할 수 있도록 도와주는
# 공통 사용할 것~~~~~~~~~~~~~~~~~

class HomeView(TemplateView):
    template_name = 'home.html'

#--- User Creation
class UserCreateView(CreateView):
 template_name = 'registration/register.html'
 form_class = UserCreationForm
 success_url = reverse_lazy('register_done')
 # 회원가입 성공시 들어갈 url


class UserCreateDoneTV(TemplateView):
 template_name = 'registration/register_done.html'

 # 성공시 축하 메시지 보내는 템플릿~