from django.urls import path
from . import views
urlpatterns = [
    path('covids', views.covids , name="covids"),
]