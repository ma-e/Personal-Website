from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.cnIndex, name='cn'),
    path('<str:name>/',views.cnBlog_detail,name = "cn_blog"),
    path('portfolio/<str:name>',views.cn_portfolio,name = "cn_portfolio"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

