from django.urls import path
from .views.photoView import PhotoView, PhotoGet

urlpatterns = [
    path('<str:tid>', PhotoGet.as_view()),
    path('list/<str:tid>', PhotoView.as_view()),
]

