from django.urls import path, include
from .views import *

app_name = 'main'

urlpatterns = [
    path('', show, name="show"),
    path('new/', new, name="new"),
    path('edit/<int:pk>', edit, name="edit"),
    path('delete/<int:pk>', delete, name="delete"),
]
