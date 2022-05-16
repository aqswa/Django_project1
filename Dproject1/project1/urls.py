"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('<int:pk>', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('<int:pk>/delete', views.delete, name="delete"),
    path('<int:pk>/update', views.update, name="update"),
    path('<int:pk>/comment', views.comment_create, name="comment_create"),
    path('<int:post_pk>/comment/<int:comment_pk>/delete',
         views.comment_delete, name="comment_delete"),
    path('common/', include('common.urls')),
    path('<int:post_pk>/like/', views.like, name="like"),
]
