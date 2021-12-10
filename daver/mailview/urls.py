from django.urls import path

from . import views

urlpatterns = [
    path('', views.mail),
    path('<int:pk>/', views.mail_detail),
]
