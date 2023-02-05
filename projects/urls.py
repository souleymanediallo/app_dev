from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects', views.project_list, name="project-list"),
    path('detail/<str:pk>', views.project_detail, name="project-detail"),
    path('update/<str:pk>', views.project_update, name="project-update"),
    path('delete/<str:pk>', views.project_delete, name="project-delete"),
    path('new', views.project_create, name="project-create"),
]