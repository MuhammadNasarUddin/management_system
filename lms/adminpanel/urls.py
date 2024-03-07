# adminpanel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_signin, name='admin_signin'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.admin_home, name='dashboard'),
    path('users/', views.admin_allusers, name='users'),
    path('interviews/', views.all_interviews, name='interviews'),
    path('faceless/', views.all_faceless, name='faceless'),
    path('posting/', views.all_posting, name='posting'),
    path('graphics/', views.all_graphics, name='graphics'),
    path('all_users_detail/<int:id>/', views.all_users_detail, name='all_users_detail'),
    path('all_user_delete/<int:id>/', views.all_user_delete, name='delete_user'),
    path('all_user_edit/<int:id>/', views.all_user_edit, name='edit_user'),
    path('all_interview_delete/<int:id>/', views.delete_interview, name='delete_interview'),
    path('all_faceless_delete/<int:id>/', views.delete_faceless, name='delete_faceless'),
    path('all_posting_delete/<int:id>/', views.delete_posting, name='delete_posting'),
    path('all_graphics_delete/<int:id>/', views.delete_graphics, name='delete_graphics'),
]
