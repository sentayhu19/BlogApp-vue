from django.urls import path
from .views import UserView

urlpatterns = [ 
    path('user/', UserView.as_view(), name = "user"),
]