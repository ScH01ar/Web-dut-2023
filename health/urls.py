from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path('news/', views.news, name='news'),
    path('exercise_check_in', views.exercise_check_in,
         name='exercise_check_in'),


    # path("create", views.create, name="create")
]
