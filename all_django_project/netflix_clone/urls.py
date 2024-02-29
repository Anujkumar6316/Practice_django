from django.urls import path
from netflix_clone import views
from django.contrib.auth import views as auth_views

app_name = 'netflix_clone'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',auth_views.LoginView.as_view(template_name='netflix_clone/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='netflix_clone/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('browse/', views.browse, name='browse'),
    path('tvshow/', views.tvshow, name='tvshow'),
    path('movies/', views.movies, name='movies'),
    path('latest/', views.latest, name='latest'),
    path('mylist/', views.mylist, name='mylist'),
    path('search/', views.search, name='search'),
    path('home/', views.home, name='home'),
    path('logout_page/',views.logout_page, name='logout_page'),
    path('single/',views.single, name='single'),
]