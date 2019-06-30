from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.FeedView.as_view(), name='index'),
]