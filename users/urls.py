from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>', views.profile, name="profile"),
    path('login', views.loginPage, name="login"),
    path("logout", views.logoutPage, name="logout"),
    path("register", views.registerUser, name="register"),
    path("account", views.userAccount, name="account"),
    path("account/update", views.accountUpdate, name="account-update"),
    path("skill/create", views.skill_create, name="skill-create"),
    path("skill/update/<str:pk>", views.skill_update, name="skill-update"),
    path("skill/delete/<str:pk>", views.skill_delete, name="skill-delete"),
]
