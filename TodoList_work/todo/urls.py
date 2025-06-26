from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo', views.todo, name='todo'), 
    path('create', views.create, name='create'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'), 
    path('ing', views.ing, name='ing'),
    path('done', views.done, name='done'),
    path('wait', views.wait, name='wait'),
]