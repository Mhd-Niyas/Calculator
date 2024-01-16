from django.urls import path
from Calc import views

urlpatterns = [
    path('',views.Calculator,name="Calculator"),
]