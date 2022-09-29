from django.urls import path
from . import views

urlpatterns = [
    path('',views.supers_list),
    path('<int:pk>/',views.individual_super),
    path('<int:pk>/powers/<int:set_power>/',views.add_power_to_super),
    path('battle/',views.fight_between_supers),
]