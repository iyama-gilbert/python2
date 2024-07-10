from django.urls import path
from . import views
urlpatterns = [
    path('', views.okaasai_list),
]

