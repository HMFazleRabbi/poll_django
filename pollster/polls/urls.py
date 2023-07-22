from django.urls import path
from . import views

app_name = 'polls' # For namespace purpose

urlpatterns=[
    path('', views.index, name='index')
]

