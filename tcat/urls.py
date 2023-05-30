from django.urls import path
from . import views

app_name = 'tcat'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tcat_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
]