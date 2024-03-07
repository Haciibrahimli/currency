from django.urls import path
from currency.views import index_view

urlpatterns = [
    path("", index_view, name='index'),
]