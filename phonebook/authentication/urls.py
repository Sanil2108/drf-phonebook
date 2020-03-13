from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.UserDetail.as_view()),
    path('contacts/', views.AllContactsView.as_view())
]