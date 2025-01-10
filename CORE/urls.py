from django.urls import path
from django.contrib.auth import views as auth_view
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout, name='logout'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login'),
]