# urls file in location


from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.homepage, name='views_homepage'),
]
