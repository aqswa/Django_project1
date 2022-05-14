from django.urls import URLPattern


from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [
    # 템플릿 지정하지 않으면 registration 템플릿 디렉토리에서 login.html을 찾음.
    #path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
]
