from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('menu/<str:name>',views.homeMenu,name='homeMenu')

]
