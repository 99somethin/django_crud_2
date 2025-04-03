from django.urls import path
from apps.news import views

urlpatterns = [
    path('', views.NewsMainPageView.as_view(), name='news_page'),
    path('crate/', views.CreatePageView.as_view(), name='create'),
    path('<int:pk>', views.SelectNewsPageView.as_view(), name='select_news'),
    path('<int:pk>/update/', views.UpdateNewsPageView.as_view(), name='update_news'),
    path('<int:pk>/delete/', views.DeleteNewsPageView.as_view(), name='delete_news'),
]