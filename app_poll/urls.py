from django.urls import path
from app_poll import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.create_user, name='register'),
    path('polls_list/', views.polls_list, name='polls_list'),

]