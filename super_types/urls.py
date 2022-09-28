from django.urls import path
from . import views

urlpatterns = [
    path('',views.types_list),
    path('<int:pk>/',views.individual_type),
]