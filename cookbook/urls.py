from django.urls import path
from .views import receipe_view

urlpatterns = [
    path('', receipe_view, name='recipe')
]
