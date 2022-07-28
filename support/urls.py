from django.urls import path

from . import views

urlpatterns = [
    path('networking/', views.networking, name="networking"),
    path('index/', views.index, name='index'),
    path('workshop/', views.workshop, name='workshop'),
    path('add_task', views.add_task, name='add_task'),
    path('edit', views.Edit, name='edit'),
    path('task_text', views.task_text, name='task_text'),
    # path('task_excel', views.task_excel, name='task_excel'),
    path('task_csv', views.task_csv, name='task_csv'),
    path('task_pdf', views.task_pdf, name='task_pdf'),
    path('search_task', views.search_task, name='search_task'),
]
