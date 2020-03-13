from django.urls import path
from records import views

urlpatterns = [
    path('', views.ContactView.as_view())
]