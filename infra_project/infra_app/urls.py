from django.urls import path
from django.contrib import admin # добавлено
from . import views

app_name = 'infra_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('second/', views.second_page, name='second_page'),
    path('admin/', admin.site.urls), # добавлено
]
