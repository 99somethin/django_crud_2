from django.urls import path
from apps.main import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('about/', views.AboutPageView.as_view(), name='about_page'),
]