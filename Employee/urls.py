from django.urls import path,include
from . import views

urlpatterns = [
    path('create_employee/',views.create_employee,name='create_employee'),
    path('search_employee/',views.search_employee,name='search_employee'),
    path('delete_employee/<int:id>',views.delete_employee,name='delete_employee'),
    path('update_employee/<int:id>',views.update_employee,name='update_employee'),
    path('do_update_employee/<int:id>',views.do_update_employee,name='do_update_employee'),

]
