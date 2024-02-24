from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.signup,name='signup'),
    # path('',include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
]