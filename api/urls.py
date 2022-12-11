from django.urls import path

from .views import bbs, BbDetailView, comments

urlpatterns = [
    path('bbs/<int:pk>/comments', BbDetailView.as_view()),
    path('bbs/<int:pk>/', comments),
    path('bbs/', bbs),
]
