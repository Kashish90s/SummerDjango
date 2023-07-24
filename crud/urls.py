from django.urls import path
# from django.urls import path
from .views import homepage,create

urlpatterns = [
    path("",homepage),
    path("create/",create)
]