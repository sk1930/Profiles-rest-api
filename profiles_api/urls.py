from django.urls import path

from profiles_api import views
# this can also be wriiten s=as
# from . import views



urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]