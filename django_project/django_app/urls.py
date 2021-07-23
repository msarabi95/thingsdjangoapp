from django.urls import path

from django_app import views

app_name = 'django_app'

urlpatterns = [
    path('', views.ThingList.as_view(), name="thing-list"),
    path('<int:pk>/', views.ThingDetail.as_view(), name="thing-detail"),
]