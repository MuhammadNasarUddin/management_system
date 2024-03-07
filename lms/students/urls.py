from django.urls import path
from . import views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('accounts/login/', views.signin, name='signin'),
    path('', views.index, name='index'),
    path("signin/",views.signin, name="signin"),
    path("signup/",views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("interview/", views.interview, name="interview"),
    path("user_interviews/", views.user_interviews, name="user_interviews"),
    path("faceless/", views.faceless, name="faceless"),
    path("user_faceless/", views.user_faceless, name="user_faceless"),
    path("posting/", views.posting, name="posting"),
    path("user_posting/", views.user_posting, name="user_posting"),
    path("graphic/", views.graphic, name="graphic"),
    path("user_graphic/", views.user_graphic, name="user_graphic"),
    path("profile/",views.profile, name="Profile")
    
]

