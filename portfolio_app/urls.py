
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('userportfolio/', views.userportfolio, name='portfolio'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/',views.profile,name='profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('update_workexperience/',views.update_workexperience,name='update_workexperience'),
    path('update_education/', views.update_education, name='update_education'),
    path('update_certificate/', views.update_certificate, name='update_certificate'),
    path('user_profile_view/',views.user_profile_view,name="user_profile_view"),
    path('logout/',views.logout,name='logout'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),

    path('projects/', views.project_list, name='project_list'),
    path('create_project/', views.create_project, name='create_project'),
    path('update_project/<int:pk>/edit/', views.update_project, name='update_project'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
]
