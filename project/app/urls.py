from django.contrib import admin

app_name='app'
from django.urls import path

from app import views

urlpatterns = [

    path('',views.function,name='function'),
    path('movie/<int:id>/',views.detail,name='det'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
