from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/<str:username>',views.sayhello),
]