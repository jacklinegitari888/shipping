from .views import get_time, hello
from django.urls import path

urlpatterns = [
   path("",hello),
   path("time/",get_time)
]
