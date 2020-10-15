from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),
    path('add', views.task_add, name='add'),
    path('delete/<id>', views.task_delete, name='delete'),
    path('delete_all/', views.task_delete_all, name='deleteall'),
    path('delete_completed/', views.task_delete_completed, name='deletecompleted'),
    path('complete/<id>', views.task_complete, name='complete'),
]