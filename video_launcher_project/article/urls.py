from django.urls import path
from .views import UserView

app_name = "user"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('user/', UserView.as_view()),
    path('user/<int:pk>', UserView.as_view()),
]