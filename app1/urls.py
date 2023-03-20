from django.urls import path

from app1 import views

urlpatterns = [
    path('',views.kidkinder,name='kidkinder'),
    path('add_todo',views.add_todo,name='add_todo'),
    path('view_todo',views.view_todo,name='view_todo'),
    path('update_todo/<int:id>/',views.update_todo,name='update_todo'),
    path('delete_todo/<int:id>/',views.delete_todo,name='delete_todo'),
]