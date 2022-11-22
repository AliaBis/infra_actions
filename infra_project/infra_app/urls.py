# from django.contrib import admin
from django.urls import path

from . import views

app_name = 'infra_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('second_page/', views.second_page, name='second_page'),  # добавлено _page
    #path('admin/', admin.site.urls),
]
