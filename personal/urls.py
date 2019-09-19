from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('portfolio/<str:name>',views.portfolio,name = "portfolio"),
    ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

