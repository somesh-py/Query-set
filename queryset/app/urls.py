from django.urls import path
from .  import views

urlpatterns = [
    path('',views.all_data),
    path('object/',views.all_data_object),
]
