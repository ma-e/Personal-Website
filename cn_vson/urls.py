from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.cnIndex, name='cn'),
    path('<str:name>/',views.cnBlog_detail,name = "cn_blog"),
    path('portfolio/游戏/',views.cn_portfolio_game,name = "cn_portfolio_game"),
    path('portfolio/<str:name>',views.cn_portfolio,name = "cn_portfolio"),
    # path('portfolio/游戏/',views.cn_portfolio_game,name = "cn_portfolio_game"),
    path('portfolio/<str:name>/',views.cn_portfolio_painting,name = "cn_portfolio_painting"),
    path('portfolio/<str:name>/',views.cn_portfolio_photo,name = "cn_portfolio_photo"),
    path('portfolio/<str:name>/',views.cn_portfolio_other,name = "cn_portfolio_other"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

