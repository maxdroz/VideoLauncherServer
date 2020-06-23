from django.urls import path

from .views import ReqView

urlpatterns = [
    path('', ReqView.as_view())
]