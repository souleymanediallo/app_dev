from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects', views.project_list, name="project-list"),
    path('detail/<str:pk>', views.project_detail, name="project-detail"),
]