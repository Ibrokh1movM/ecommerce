from django.urls import path, include
from user import views

app_name = 'user'

urlpatterns = [
    path('login-oauth-page/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path("register/", views.register, name="register"),
    path('verify/', views.verify_email, name='verify'),
]
