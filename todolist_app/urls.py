from todolist_app import views
from django.urls import path

urlpatterns = [
    path('',views.todolist,name='todolist'),
    path('delete/<bucin_id>/',views.delete_task,name='delete_task'),
    path('edit/<bucin_id>/',views.edit_task,name='edit_task'),
    path('complete/<bucin_id>/',views.complete_task,name='complete_task'),
    path('pending/<bucin_id>/',views.pending_task,name='pending_task'),

    

]
