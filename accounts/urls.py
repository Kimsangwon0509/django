from django.urls import path, include
from . import views
from rest_framework import urls

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('api-auth/', include(urls)),
]
