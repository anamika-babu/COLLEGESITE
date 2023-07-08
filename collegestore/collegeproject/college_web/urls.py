from django.urls import path
from .import views

urlpatterns = [

    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('newpage/',views.newpage,name='newpage'),
    path('detailform',views.detailform,name='detailform'),
    path('logout', views.logout, name='logout'),

]