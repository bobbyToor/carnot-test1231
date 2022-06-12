from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('student/', views.student),
    path('student/<int:id>/', views.student_data),
    path('student/create/', views.student_create_page),

    path('search/', views.student_search_page),
]
