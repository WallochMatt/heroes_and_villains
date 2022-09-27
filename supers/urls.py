from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.supers_list),
]
    #path('',views.supers_list),