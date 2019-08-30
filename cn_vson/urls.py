from django.urls import path

from . import views


urlpatterns = [
    path('', views.cnIndex, name='cn'),
    path('<str:name>/',views.cnBlog_detail, name = "cn_blog")
]