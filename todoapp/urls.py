from django.urls import path
from .views import *

urlpatterns = [
    path('getpost/',TodosView.as_view(),name='getpost'),
    path('byid/<int:pk>/',TodosById.as_view(),name='byid'),
]
