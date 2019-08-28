from django.contrib import admin
from django.conf.urls import url,include
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('personal.urls')), 
    path('cn/', include('cn_vson.urls')), 
]