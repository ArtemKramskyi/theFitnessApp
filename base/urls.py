from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('search', views.search_exercise, name='search'),
    path('addProgram', views.add_program, name='addProgram'),
    path('addExercise', views.add_exercise, name='addExercise'),
    path('myPrograms', views.programs_view, name='myPrograms'),
    path('editProgram', views.edit_program, name='editProgram'),
    path('deleteProgram', views.delete_program, name='deleteProgram'),
    path('deleteExercise', views.delete_exercise, name='deleteExercise'),
    path('program/<str:pk>/', views.program_page, name='programPage')
]
