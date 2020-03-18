
from django.contrib import admin
from personal.models import *
                           
admin.site.register([Portfolio,Blog,Bio,Portfolio_game,Portfolio_painting,\
                    Portfolio_photo,Portfolio_other,Comment,Project])